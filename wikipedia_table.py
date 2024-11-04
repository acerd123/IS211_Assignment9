
# https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
import requests
from bs4 import BeautifulSoup

# URL for the Wikipedia page containing Super Bowl Champions
url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'

def clean_text(text):
    """Clean the text by removing footnotes and unwanted characters."""
    return text.split('[')[0].strip()  # Remove footnote references

def scrape_super_bowl_champions():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all tables on the page
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables on the page.")

        # Extract data from Table 2
        champions_table = tables[1]  # Table 2 based on zero-indexing
        
        # Get headers
        headers = [header.text.strip() for header in champions_table.find_all('th')]
        print(f"Headers: {headers}")

        # Iterate over each row in the table
        for row in champions_table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if columns:  # Only process rows with data
                row_data = [clean_text(column.text) for column in columns]
                print(row_data)  # Print each cleaned row's data

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper for Wikipedia Table of Super Bowl Champions")
    scrape_super_bowl_champions()

