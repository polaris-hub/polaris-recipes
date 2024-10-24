import requests
from bs4 import BeautifulSoup
from itertools import product
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
import time
import pandas as pd
import os
# Base URL for the search page
base_url = "https://www.addgene.org/search/catalog/plasmids/"

# Parameters for the request
params_template = {
    'page_number': 1,
    'page_size': 50,  # Adjust page size if necessary
    'q': ''  # This will be filled with each search query
}

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

MAX_RETRIES = 5   # Maximum number of retries for 429 errors
BACKOFF_FACTOR = 2  # Backoff factor for exponential backoff
REQUEST_DELAY = 0.5  # Fixed delay between requests (in seconds) to prevent hitting rate limits

# Function to fetch plasmid data for a single query
def fetch_plasmid_data_for_combo(combo):
    encountered_ids = set()
    params = params_template.copy()
    params['q'] = combo
    params['page_number'] = 1
    plasmid_data = []

    retries = 0

    while True:  # Stop after reaching the 240th page
        try:
            # Delay between requests to prevent rate limiting
            time.sleep(REQUEST_DELAY)

            # Send GET request to the search URL
            response = requests.get(base_url, headers=headers, params=params)
            
            # Check if the request was successful
            response.raise_for_status()

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all plasmids on the current page
            plasmids = soup.find_all('article')

            for plasmid in plasmids:
                # Extract plasmid ID using the correct method you provided
                plasmid_id = plasmid.find('div', class_='col-xs-10').text.strip().strip("#")

                if plasmid_id not in encountered_ids:
                    encountered_ids.add(plasmid_id)
                    plasmid_data.append(plasmid_id)  # Store the plasmid data

            # Check if there's a next page
            next_button = soup.find('li', class_='next-btn')
            if next_button and 'disabled' not in next_button.get('class', []):
                params['page_number'] += 1
                retries = 0
            else:
                break
        except requests.exceptions.HTTPError as e:
            # Handle 429 Too Many Requests error with retries
            if response.status_code == 429:
                if retries < MAX_RETRIES:
                    # Exponential backoff
                    wait_time = BACKOFF_FACTOR ** retries
                    print(f"429 Too Many Requests for query '{combo}' - waiting {wait_time}...", file=sys.stderr)
                    time.sleep(wait_time)
                    retries += 1
                    continue
                else:
                    print(f"Max retries reached for query '{combo}' after 429 error.", file=sys.stderr)
                    break
            else:
                print(f"Error occurred for query '{combo}': {e}", file=sys.stderr)
                break  # Break out of the loop on other HTTP errors

    return plasmid_data

def parallel_scrape(max_workers):
    # Generate all combinations of four digits (1000 to 9999)
    combinations = [''.join(map(str, c)) for c in product(range(1, 10), range(10), range(10), range(10))]

    all_plasmid_data = []

    # Use ThreadPoolExecutor to parallelize the work
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks to the executor
        futures = {executor.submit(fetch_plasmid_data_for_combo, combo): combo for combo in combinations}

        # Collect results as they complete
        for future in as_completed(futures):
            combo = futures[future]
            try:
                data = future.result()
                all_plasmid_data.extend(data)
                print(f"Finished query '{combo}', retrieved {len(data)} plasmid IDs.")
            except Exception as e:
                print(f"Error with combo '{combo}': {e}", file=sys.stderr)

    return list(set(all_plasmid_data))

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Scrape plasmid IDs from Addgene.")
    parser.add_argument(
        "--workers", type=int, default=5, help="Number of threads to use for parallel scraping (default: 5)"
    )

    args = parser.parse_args()

    # Run the parallel scraping function
    plasmid_data = parallel_scrape(args.workers)

    plasmid_data = pd.DataFrame(plasmid_data, columns=['ID'])
    # make directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    plasmid_data.to_csv("data/plasmid_ids.txt", index=False)

    print(f"All unique plasmid IDs have been saved to 'data/plasmid_ids.txt'.")

if __name__ == "__main__":
    main()
