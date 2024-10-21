import requests
from bs4 import BeautifulSoup
import csv

# Fetch the webpage
response = requests.get("https://gravityfalls.fandom.com/wiki/Season_1")

soup = BeautifulSoup(response.text, 'html.parser')
episodes = []

    # Find the table that has episode data
table = soup.find('table', style="border-collapse:collapse; color: #000; width:100%; background:#fff7f7; border-color:#aaa;")
    

tbody = table.find('tbody')  # Find the tbody element

    # Iterate through each row in the tbody
for row in tbody.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    if len(columns) >= 5:  # Ensure there are enough columns
        # Extract episode number, title, and viewer rating
        episode_number = columns[0].text.strip()  # Episode number
        title = columns[2].find('a')['title'] if columns[2].find('a') else 'N/A'  # Episode title
        viewer_rating = columns[5].text.strip() if len(columns) > 5 else 'N/A'  # Viewer rating
                
                # Append the episode data to the list
        episodes.append([episode_number, title, viewer_rating])
        print(f"Extracted {len(episodes)} episodes from Season 1.")
        # Write to a CSV file
with open('gravity_falls_season_1_episodes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Episode Number', 'Title', 'Viewer Rating'])  # Write the header
    writer.writerows(episodes)  # Write all episode data as rows


 






    

