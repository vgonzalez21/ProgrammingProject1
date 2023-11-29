import requests
from bs4 import BeautifulSoup as bs

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = requests.get(wiki)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())