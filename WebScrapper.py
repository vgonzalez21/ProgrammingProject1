import requests as rq
from bs4 import BeautifulSoup as bs

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = rq.get(wiki)
#print(page.text) not readable
soup = bs(page.text, 'html.parser')

#print(soup) better but cant do much
#print(soup.prettify()) #little better

#print(soup.td.string)

right_table = soup.find('table', class_='wikitable sortable')
print(right_table)
a, b, c, d, e, f, g = [], [], [], [], [], [], []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(states) != 0:
        print(states[0])

    if len(cells) == 6:
        a.append(cells[0].find(string='TRUE'))
        b.append(states[0].find(string=TRUE))
        c.append(cells[1].find(string=TRUE))
        d.append(cells[2].find(string=TRUE))
        e.append(cells[3].find(string=TRUE))
        f.append(cells[4].find(string=TRUE))
        g.append(cells[5].find(string=TRUE))

"""
import pandas as pd

df=pd.DataFrame(a, columns=['Number'])
df['State/UT'] = b
df['Admin_Capital'] = c
df['Legislative_Capital'] = d
df['Judiciary_Capital'] =e
df['Year_Capital'] = f
df['Former_Capital'] = g
df
"""