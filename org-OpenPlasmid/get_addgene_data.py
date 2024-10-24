import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import os
import threading
import concurrent.futures 
from datasets import load_dataset

def download_genbank(genbank_file):
    if genbank_file:
        response = requests.get(genbank_file)
        if response.status_code == 200:
            return response.text
    return None

# Clean text by removing excessive spaces and unwanted content
def clean_text(text):
    return ' '.join(text.split()).strip().replace('(How to cite)', '')

# Fetch and parse the webpage content
def fetch_page_content(plasmid_id):
    url = f"https://www.addgene.org/{plasmid_id}/"
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

# Generic function to extract data based on element class or id
def extract_text(soup, identifier, tag='div', attr='class', fallback=None):
    element = soup.find(tag, {attr: identifier})
    return clean_text(element.get_text(strip=True)) if element else fallback

# Extract the flame status (high, medium, or low) based on class
def extract_flame_status(soup):
    flame_container = soup.find('div', id='plasmid-flame-container')
    if flame_container:
        flame_tag = flame_container.find('span', class_='addgene-flame-with-popover')
        if flame_tag:
            if 'addgene-flame-high' in flame_tag['class']:
                return 'High'
            elif 'addgene-flame-medium' in flame_tag['class']:
                return 'Medium'
            elif 'addgene-flame-low' in flame_tag['class']:
                return 'Low'
    return None

# Extract key-value pairs like Depositing Lab and Publication
def extract_field_label_content(soup, label_text):
    label = soup.find('div', class_='field-label', string=label_text)
    if label:
        content = label.find_next('div', class_='field-content')
        return clean_text(content.get_text(strip=True)) if content else None
    return None

def get_sequence(plasmid_id):
    sequence_url = f"https://www.addgene.org/{plasmid_id}/sequences/"
    response = requests.get(sequence_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        sequence_type = None
        genbank_link = None

        # Priority order: Addgene full, Depositor full, Addgene partial, Depositor partial
        for section_id in ['addgene-full', 'depositor-full', 'addgene-partial', 'depositor-partial']:
            sequence_type = 'full' if 'full' in section_id else 'partial'
            section = soup.find('section', {'id': section_id})
            if section:
                genbank_tag = section.find('a', {'class': 'genbank-file-download'})
                if genbank_tag:
                    genbank_link = genbank_tag['href']
                break  # Exit loop if sequence is found

        return genbank_link, sequence_type
    
    return None, None, None, None

# Extract GenBank and SnapGene file links
def extract_file_links(soup, plasmid_id):
    files = {'GenBank File': None}
    genbank_link = soup.find('a', class_='genbank-file-download')
    if genbank_link:
        files['GenBank File'] = genbank_link['href']
        files['Sequence Type'] = 'full'
    else:
        genbank_link, sequence_type = get_sequence(plasmid_id)
        files['GenBank File'] = genbank_link
        files['Sequence Type'] = sequence_type
    
    return files

# Extract content from sections based on <h2> headers
def extract_sections(soup):
    sections = {}
   
    for section_header in soup.find_all('h2'):
        section_title = clean_text(section_header.get_text(strip=True))
        
        if section_title.startswith('Information for'):
            continue
        section_data = {}

        # Find the next <ul> after the <h2> tag (if present)
        ul_tag = section_header.find_next('ul')
        if ul_tag:
            for li in ul_tag.find_all('li', class_='field'):
                label = li.find('div', class_='field-label') or li.find('span', class_='field-label')
                if label:
                    label_text = clean_text(label.get_text(strip=True))
                    value = label.find_next_sibling(string=True).strip() if label.find_next_sibling(string=True) else ''
                    
                    # Check for nested <ul> for additional values
                    nested_ul = li.find('ul', class_='addgene-document-list')
                    if nested_ul:
                        nested_values = [clean_text(nested_li.get_text(strip=True)) for nested_li in nested_ul.find_all('li')]
                        value = " ; ".join(nested_values)  # Join nested values with a semicolon

                    # Check for an anchor tag for Entrez Gene symbol
                    gene_symbol_tag = li.find('span', class_='gene-symbol')
                    if gene_symbol_tag:
                        value = gene_symbol_tag.get_text(strip=True) # Extract gene symbol

                    # Store the extracted value
                    section_data[label_text] = clean_text(value)

        # Add section data if available
        if section_data:
            # So as not to create duplicate columns
            if section_title == 'Gene/Insert':
                section_title += ' 1'
            elif section_title == 'Cloning Information':
                section_title += ' for Gene/Insert 1'

            sections[section_title] = section_data
    
    return sections

# Extract Depositor Comments
def extract_depositor_comments(soup):
    notes_section = soup.find('div', id='notes-sections')
    if notes_section:
        depositor_comments_header = notes_section.find('h2', string='Depositor Comments')
        if depositor_comments_header:
            depositor_comments_data = ""
            for p in depositor_comments_header.find_next('div').find_all('p'):
                depositor_comments_data += p.get_text(strip=True) + " "
            return depositor_comments_data.strip()
    return None

def extract_references(soup):
    ref_data = None
    
    # Loop through all <p> tags to find the one containing "For your References section"
    for p_tag in soup.find_all('p'):
        if "For your References section" in p_tag.get_text():
            # Find the associated div that follows the paragraph
            ref_section = p_tag.find_next_sibling('div', class_='indent well well-sm')
            if ref_section:
                cite = ref_section.find('cite')
                if cite:
                    ref_data = {}
                    
                    # Extract the reference title from <strong>
                    ref_data['Title'] = clean_text(cite.find('strong').get_text(strip=True)) if cite.find('strong') else ''
                    
                    # Extract the publication information from <i> tag
                    publication_info = cite.find('i')
                    if publication_info:
                        pub_text = publication_info.get_text(strip=True)
                        ref_data['Publication'] = clean_text(pub_text)
                    
                    # Extract the DOI (numeric format after publication info)
                    full_text = cite.get_text(separator=" ", strip=True)
                    doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', full_text, re.I)
                    ref_data['DOI'] = doi_match.group(0) if doi_match else ''
                    
                    # Remove title, publication, DOI, and PubMed text from authors' section
                    authors_text = full_text.replace(ref_data['Title'], '')
                    authors_text = authors_text.replace(ref_data['Publication'], '')
                    authors_text = authors_text.replace(ref_data['DOI'], '')
                    authors_text = re.sub(r'\d+', '', authors_text)  # Remove any numeric values (e.g., PubMed ID)
                    authors_text = authors_text.replace("PubMed", '').strip()  # Remove 'PubMed' keyword
                    authors_text = authors_text.replace(".", "").strip()

                    # Set the cleaned remaining text as authors
                    ref_data['Authors'] = clean_text(authors_text)
                    
                    # Extract the PubMed link and PubMed ID
                    pubmed_link = cite.find('a', href=True)
                    if pubmed_link:
                        ref_data['PubMed Link'] = pubmed_link['href']
                        ref_data['PubMed ID'] = clean_text(pubmed_link.get_text(strip=True))
    
    return ref_data

def check_expected_keys(scrape_dict):
    # Define the expected keys and their nested keys
    expected_structure = {
        'Backbone': [
            'Vector backbone',
            'Backbone size w/o insert (bp)',
            'Vector type',
            'Selectable markers'
        ],
        'Growth in Bacteria': [
            'Bacterial Resistance(s)',
            'Growth Temperature',
            'Growth Strain(s)',
            'Copy number'
        ],
        'Terms and Licenses': [
            'Academic/Nonprofit Terms',
            'Industry Terms'
        ],
        'References': [
            'Title',
            'Publication',
            'DOI',
            'Authors',
            'PubMed Link',
            'PubMed ID'
        ],
        'Gene/Insert 1': [
            'Gene/Insert name',
            'Species',
            'Insert Size (bp)',
            'Mutation',
            'Entrez Gene',
            'Promoter',
            'Tag / Fusion Protein'
        ],
        'Cloning Information for Gene/Insert 1': [
            'Cloning method',
            '5′ cloning site',
            '3′ cloning site',
            '5′ sequencing primer',
            '3′ sequencing primer'
        ],
        'Gene/Insert 2': [
            'Gene/Insert name',
            'Species',
            'Insert Size (bp)',
            'Mutation',
            'Entrez Gene',
            'Promoter',
            'Tag / Fusion Protein'
        ],
        'Cloning Information for Gene/Insert 2': [
            'Cloning method',
            '5′ cloning site',
            '3′ cloning site',
            '5′ sequencing primer',
            '3′ sequencing primer'
        ],
        'Gene/Insert 3': [
            'Gene/Insert name',
            'Species',
            'Insert Size (bp)',
            'Mutation',
            'Entrez Gene',
            'Promoter',
            'Tag / Fusion Protein'
        ],
        'Cloning Information for Gene/Insert 3': [
            'Cloning method',
            '5′ cloning site',
            '3′ cloning site',
            '5′ sequencing primer',
            '3′ sequencing primer'
        ]
    }

    # Initialize or update nested dictionaries and subkeys
    for key, subkeys in expected_structure.items():
        new_subdict = {}
        if key in scrape_dict and isinstance(scrape_dict[key], dict):
            # Existing subdictionary
            existing_subdict = scrape_dict[key]
            # Remove keys not in subkeys and convert values to strings
            for subkey in subkeys:
                value = existing_subdict.get(subkey, '')
                new_subdict[subkey] = str(value) if value is not None else ''
        else:
            # Missing or invalid subdictionary, initialize with empty strings
            new_subdict = {subkey: '' for subkey in subkeys}
        # Replace the subdictionary in scrape_dict
        scrape_dict[key] = new_subdict

    # Define other non-dictionary expected keys
    expected_keys = [
        'Name',
        'ID',
        'Flame',
        'Purpose',
        'Depositing Lab',
        'Publication',
        'GenBank File',
        'Sequence Type',
        'GenBank Raw'
    ]

    # Add missing non-dictionary keys and convert existing values to strings
    for key in expected_keys:
        if key in scrape_dict:
            # Convert existing value to string
            value = scrape_dict[key]
            scrape_dict[key] = str(value) if value is not None else ''
        else:
            scrape_dict[key] = ''

    # Combine both dictionary keys and other keys into one list
    full_expected_keys = expected_keys + list(expected_structure.keys())

    # Remove any keys not in the expected list
    scrape_dict = {key: scrape_dict[key] for key in full_expected_keys if key in scrape_dict}

    # Order the keys as full_expected_keys
    scrape_dict = {key: scrape_dict[key] for key in full_expected_keys}

    return scrape_dict


def convert_values_to_strings(data):
    if isinstance(data, dict):
        return {key: convert_values_to_strings(value) for key, value in data.items()}
    else:
        return str(data) if data is not None else ''

# Main scraping function
def scrape_general_page(plasmid_id):
    soup = fetch_page_content(plasmid_id)
    page_data = {}

    # Populate data using modular functions
    page_data['Name'] = extract_text(soup, 'material-name', tag='span')
    page_data['ID'] = extract_text(soup, 'addgene-item-id', tag='span', attr='id')
    page_data['Flame'] = extract_flame_status(soup)
    page_data['Purpose'] = extract_field_label_content(soup, 'Purpose')
    page_data['Depositing Lab'] = extract_field_label_content(soup, 'Depositing Lab')
    page_data['Publication'] = extract_field_label_content(soup, 'Publication')
    page_data.update(extract_file_links(soup, plasmid_id))
    page_data.update(extract_sections(soup))
    page_data['Depositor Comments'] = extract_depositor_comments(soup)
    page_data['References'] = extract_references(soup)
    page_data['GenBank Raw'] = download_genbank(page_data['GenBank File'])
    page_data = check_expected_keys(page_data)
    page_data = convert_values_to_strings(page_data)

    return page_data

# Load existing results from JSON Lines file and extract 'ID' values
def load_existing_results(filename):
    ids = []
    if os.path.exists(filename):
        data = load_dataset("json", data_files=filename)
        ids = [x['ID'] for x in data['train']]
    return ids

# Thread-safe function to write results to JSON Lines file
def write_result_to_file(data, lock):
    with lock:
        with open('data/results.jsonl', 'a') as jsonl_file:
            jsonl_file.write(json.dumps(data) + '\n')

# Main function to read plasmid IDs and scrape data in parallel
def main():
    results_file = 'data/results.jsonl'
    existing_results = load_existing_results(results_file)
    plasmid_ids = pd.read_csv('data/plasmid_ids.txt')['ID'].astype(str).values
    
    # Filter out already processed plasmid IDs
    plasmid_ids = [str(plasmid_id) for plasmid_id in set(plasmid_ids) - set(existing_results)]
    print(f"Scraping {len(plasmid_ids)} plasmids...")

    lock = threading.Lock()  # Create a lock for thread-safe writing
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_id = {executor.submit(scrape_general_page, plasmid_id): plasmid_id for plasmid_id in plasmid_ids}
        for future in concurrent.futures.as_completed(future_to_id):
            plasmid_id = future_to_id[future]
            try:
                results = future.result()

                write_result_to_file(results, lock)

            except Exception as exc:
                print(f'{plasmid_id} generated an exception: {exc}')

if __name__ == "__main__":
    main()