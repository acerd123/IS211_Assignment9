# football_stats.py
import requests
from bs4 import BeautifulSoup

# URL for CBS NFL Scoring Stats
url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/'
response = requests.get(url)

# Ensure the response was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the table for the scoring stats
    table = soup.find('table')  # Simplified selector; refine based on inspection

    def scrape_football_stats():
        if table:
            # Find the top 20 players
            players = table.find_all('tr')[1:21]  # Skip header row, limit to top 20
            for player in players:
                columns = player.find_all('td')
                
                # Ensure there are enough columns to avoid index errors
                if len(columns) >= 4:
                    # Strip and clean each field to remove extra whitespace
                    name = columns[0].get_text(strip=True)
                    position = columns[1].get_text(strip=True)
                    team = columns[2].get_text(strip=True)
                    touchdowns = columns[3].get_text(strip=True)
                    
                    # Print the cleaned output
                    print(f"Name: {name}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
        else:
            print("Could not find the table on the page. The structure may have changed.")

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper one: CBS Football Stats")
    scrape_football_stats()






