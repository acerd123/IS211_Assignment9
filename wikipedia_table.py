
# https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'

def clean_text(text):
    """Clean the text by removing footnotes and unwanted characters."""
    return text.split('[')[0].strip()  

def scrape_super_bowl_champions():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables on the page.")

        
        champions_table = tables[1]  
        
        
        headers = [header.text.strip() for header in champions_table.find_all('th')]
        print(f"Headers: {headers}")

        
        for row in champions_table.find_all('tr')[1:]:  
            columns = row.find_all('td')
            if columns:  
                row_data = [clean_text(column.text) for column in columns]
                print(row_data)  

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper for Wikipedia Table of Super Bowl Champions")
    scrape_super_bowl_champions()

