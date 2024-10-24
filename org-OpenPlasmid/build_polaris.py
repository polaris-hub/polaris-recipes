import numpy as np
import pandas as pd
from datasets import load_dataset
from Bio import SeqIO
from io import StringIO
import re
from collections import Counter
from polaris.dataset import Dataset
from polaris.utils.types import HubOwner
from polaris.hub.client import PolarisHubClient
import warnings
from Bio import BiopythonParserWarning


warnings.filterwarnings("ignore", category=BiopythonParserWarning, message="Attempting to parse malformed locus line:")


def read_genbank(record: str):
    return SeqIO.read(StringIO(record), "genbank")

def load_and_preprocess_data():
    data = load_dataset("json", data_files="data/results.jsonl.gz")['train']
    # data = data.select(range(20000)) # for testin
    data = data.filter(lambda x: x['GenBank Raw'] != '')
    all_feat = data.to_pandas()
    all_feat['GenBank'] = all_feat['GenBank Raw'].map(read_genbank)
    return all_feat

def clean_gene_name(gene):
    gene = re.sub(r'^(human|mouse|rat|h|m|r)\s*', '', gene, flags=re.IGNORECASE)
    gene = re.sub(r'\s*(gene|protein)$', '', gene, flags=re.IGNORECASE)
    gene = re.sub(r'\s*\([^)]*\)', '', gene)
    
    gene_map = {
        'neo': 'neomycin resistance',
        'amp': 'ampicillin resistance',
        'gfp': 'GFP',
        'egfp': 'GFP',
        'rfp': 'RFP',
        'dsred': 'RFP',
        'kan': 'kanamycin resistance',
    }
    
    for key, value in gene_map.items():
        if re.search(rf'\b{key}\b', gene, re.IGNORECASE):
            return value
    
    return gene.strip().lower()

def extract_cds_genes(record):
    return [clean_gene_name(feature.qualifiers.get('gene', feature.qualifiers.get('product', ['']))[0])
            for feature in record.features if feature.type == 'CDS']

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence) if sequence else 0

def extract_sequence_features(all_feat):
    all_feat['CDS genes'] = all_feat['GenBank'].map(extract_cds_genes)
    all_feat['Sequence length'] = all_feat['GenBank'].map(lambda x: len(x.seq))
    all_feat['GC content'] = all_feat['GenBank'].map(lambda x: calculate_gc_content(str(x.seq)))
    return all_feat

def define_keywords(all_feat):
    feature_counts = Counter(gene for genes in all_feat['CDS genes'] for gene in genes)
    exclude = ['bla', 'op']
    return [key for key, _ in feature_counts.most_common(15) if key not in exclude][::-1]

def map_genes(genes, keywords):
    return next((keyword for keyword in keywords if any(re.search(keyword, gene, re.IGNORECASE) for gene in genes)), pd.NA)

def process_entrez_genes(all_feat):
    all_feat['Entrez genes'] = all_feat.apply(lambda row: [insert['Entrez Gene'].upper() 
                                                           for i in range(1, 4) 
                                                           for insert in [row[f'Gene/Insert {i}']] 
                                                           if isinstance(insert, dict) and insert.get('Entrez Gene')], axis=1)

    common_entrez = all_feat['Entrez genes'].explode().value_counts().head(20).index.tolist()
    common_entrez_priority = {gene: i for i, gene in enumerate(reversed(common_entrez))}

    all_feat['Entrez-curated-features'] = all_feat['Entrez genes'].apply(lambda genes: max(
        (gene for gene in genes if gene in common_entrez_priority),
        key=lambda g: common_entrez_priority[g],
        default=pd.NA
    ))
    return all_feat


def main():

    all_feat = load_and_preprocess_data()
    all_feat = extract_sequence_features(all_feat)
    
    keywords = define_keywords(all_feat)
    all_feat['CDS-curated-features'] = all_feat['CDS genes'].apply(lambda x: map_genes(x, keywords))
    
    all_feat = process_entrez_genes(all_feat)

    # prepare polaris dataset
    del all_feat['GenBank']
    table = all_feat.astype(str)
    table['ID'] = table['ID'].astype(int)

    dataset = Dataset(
        table=table,
        name="OpenPlasmid-v1",
        description="A dataset of ~150k  multi-component plasmids originally deposited on Addgene. Features include textual descriptions, depositor/study information, annotated GenBank sequences and more.",
        source="https://www.addgene.org/",
        curation_reference="https://github.com/polaris/polaris-recipes/org-OpenPlasmid",
        annotations={},
        tags=["plasmid", "genomics"],
        owner=HubOwner(user_id="wconnell", slug="wconnell"),
        license="CC-BY-4.0",
        user_attributes={"year": "2024"},
    )

    with PolarisHubClient() as client:
        client.upload_dataset(dataset=dataset)
    

if __name__ == "__main__":
    main()