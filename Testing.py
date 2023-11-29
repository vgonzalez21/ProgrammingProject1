'''import requests
from bs4 import BeautifulSoup

# Replace this URL with the URL of the website you want to scrape
url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the HTML elements containing the data you want to scrape
    # In this example, we're looking for article titles within <h2> tags
    article_titles = soup.find_all('h2')

    # Extract and print the titles
    for title in article_titles:
        print(title.text)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
'''


import requests
from bs4 import BeautifulSoup

# Replace this URL with the URL of the webpage containing the table
url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table element
    table = soup.find('table',  class_='wikitable sortable')

    if table:
        # Find the table header (titles of the columns) in the thead section
        column_titles = [header.text for header in table.thead.find_all('th')]

        # Find and iterate through table rows in the tbody section
        for row in table.tbody.find_all('tr'):
            # Find and iterate through the cells in each row
            cells = row.find_all('td')
            row_data = [cell.text for cell in cells]

            # You can now process or print the data as needed
            print("Column Titles:", column_titles)
            print("Row Data:", row_data)
    else:
        print("No table found on the webpage.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
