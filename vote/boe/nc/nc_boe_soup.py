import requests
from bs4 import BeautifulSoup as BS


# URL for NC Board of Elections
BOE_SITE = 'http://vt.ncsbe.gov/BOEInfo/PrintableVersion/'

# retrieve page
r = requests.get(BOE_SITE)

# parse using BeautifulSoup
soup = BS(r.text, "lxml")
print(soup)

# get table
table = soup.find('table', id="gridBOEInfo")
print(table)
print(table.findAll('tbody'))

for table_row in table.findAll('tr'):
    print(1)
    for table_data in table_row.findAll('td'):
        print(table_data.text)
