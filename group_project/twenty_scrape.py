
import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://americasbesthistory.com/abhtimeline2020.html"

# Fetch the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate all <br> tags and extract the text between consecutive pairs of <br> tags
br_tags = soup.find_all('br')
data = []

# Extract text between <br> tags
for i in range(len(br_tags) - 1):
    text = []
    sibling = br_tags[i].next_sibling
    while sibling and sibling != br_tags[i + 1]:
        if sibling and isinstance(sibling, str):
            text.append(sibling.strip())
        sibling = sibling.next_sibling
    if text:
        data.append(' '.join(text))

# Extract text between <h#> tags and the following <br> tag
for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    text = []
    sibling = header.next_sibling
    while sibling and sibling.name != 'br':
        if sibling and isinstance(sibling, str):
            text.append(sibling.strip())
        sibling = sibling.next_sibling
    if text:
        data.append(' '.join(text))

# Split the data into date and event details
split_data = []
for entry in data:
    if ' - ' in entry:
        date, event = entry.split(' - ', 1)
        split_data.append([date.strip(), event.strip()])

# Write the extracted text to a CSV file
with open('twenty_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Event'])  # Header
    for row in split_data:
        writer.writerow(row)