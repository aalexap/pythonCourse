import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'

full_page = requests.get(url)
soup = BS(full_page.content, 'html.parser')
table = soup.find(['tbody'])
all_trs = table.find_all('tr')

dict = {}

for tr in all_trs:
    parameters = {}
    first_td = tr.find(['td'])
    i = 0
    for i in range(10):
        parameters[i] = first_td.find_next_siblings('td')[i].text
    dict[first_td.text] = parameters
print(dict)