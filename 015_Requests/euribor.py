import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.euribor-rates.eu/en/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

full_page = requests.get(url, headers=headers)
soup = BS(full_page.content, 'html.parser')

six_month = soup.find('td', string='Euribor 6 months').find_next_sibling()
print(six_month.text)
