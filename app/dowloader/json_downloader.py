from typing import List, Optional
import requests
import sys
import os
from app.dowloader.interface import IDownloader
from app.parser.model import parse_product

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)


class JsonDownloader(IDownloader):
    def download(self, url: str, destination: str) -> Optional[List[dict]]:
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            if response.ok:
                json_data = response.json()
                products_raw = json_data.get("products", [])
                products = [parse_product(p) for p in products_raw]
                for p in products:
                    print(p)
            else:
                response.raise_for_status()  # Raise an error for bad responses
            

            # Write the content to the destination file
            with open(destination, 'w') as file:
                file.write(response.text)

            print(f"Downloaded JSON data from {url} to {destination}")
            return products
        except requests.exceptions.RequestException as e:
            print(f"Failed to download JSON data from {url}: {e}")
            return None 