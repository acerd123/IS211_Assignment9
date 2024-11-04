# https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/
import requests
from bs4 import BeautifulSoup


url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/'
response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    table = soup.find('table')  

    def scrape_football_stats():
        if table:
            
            players = table.find_all('tr')[1:21] 
            for player in players:
                columns = player.find_all('td')
                
                
                if len(columns) >= 4:
                    name = columns[0].get_text(strip=True)
                    position = columns[1].get_text(strip=True)
                    team = columns[2].get_text(strip=True)
                    touchdowns = columns[3].get_text(strip=True)
                    
                    
                    print(f"Name: {name}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
        else:
            print("Could not find the table on the page. The structure may have changed.")

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    print("Running scraper one: CBS Football Stats")
    scrape_football_stats()






