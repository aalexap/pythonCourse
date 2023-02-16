import requests
from bs4 import BeautifulSoup as BS
import re

url = 'https://gammatest.net/course/python/'
full_page = requests.get(url, timeout=3)

soup = BS(full_page.content, 'html.parser')
# print(soup.prettify())

# print(soup.title.name)
# print(soup.title.text)
# print(soup.div['class'])

# print(soup.title.parent)

# match = soup.find('div', class_='navbar-header')
# print(match.a['href'])

# match = soup.find_all('div', class_='col-md-4 col-sm-12')
# for div in match:
#     links = div.find_all('a')
#     for link in links:
#         print(link['href'])

# print(match[0])

# print(soup.find(re.compile(r'^me')))
# print(soup.find(string=re.compile(r'^Пе')))
# print(soup.find_all(['a', 'table']))

# for tag in soup.find_all(True):
#     print(tag)

# print(soup.find_all(string=True))
# print(soup.find_all('a', string='Перейти', limit=2))

test_link = soup.find('a', string='Eesti keeles')
# print(test_link.find_parents('div'))

# print(test_link.find_parent())
# print(test_link.find_next_sibling())
# print(test_link.find_previous_sibling().find_nex_sibling())
# print(soup.find('div', class_='col-md-4').find_previous_siblings())
# print(test_link.find_next())
print(test_link.find_all_next())