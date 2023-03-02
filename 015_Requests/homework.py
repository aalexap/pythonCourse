import requests
from bs4 import BeautifulSoup as BS

def check():
    if region in dict.keys():
        if dict[region][0] != '':
            print('Keskmine Õhutempetatuur: ' + dict[region][0] + '°C')
        if dict[region][1] != '':
            print('max Õhutempetatuur: ' + dict[region][1] + '°C')
        if dict[region][2] != '':
            print('min Õhutempetatuur: ' + dict[region][2] + '°C')
        if dict[region][3] != '':
            print('Maapinna minimaalne temperatuur: ' + dict[region][3] + '°C')
        if dict[region][4] != '':
            print('Minimaalne temperatuur 2cm kõrgusel maapinnast: ' + dict[region][4] + '°C')
        if dict[region][5] != '':
            print('Keskmine suhteline õhuniiskus: ' + dict[region][5] + '%')
        if dict[region][6] != '':
            print('min suhteline õhuniiskus: ' + dict[region][6] + '%')
        if dict[region][7] != '':
            print('Keskmine tuule kiirus: ' + dict[region][7] + ' m/s')
        if dict[region][8] != '':
            print('max tuule kiirus: ' + dict[region][8] + ' m/s')
        if dict[region][9] != '':
            print('Sademed: ' + dict[region][9] + ' mm')
        if dict[region][10] != '':
            print('Päikesepaiste kestus: ' + dict[region][10] + ' h')
    else:
        print('Wrong region')


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
    for i in range(11):
        parameters[i] = first_td.find_next_siblings('td')[i].text
    dict[first_td.text] = parameters

while True:
    region = input('Please region or type "EXIT": ')
    if region.lower() == 'exit':
        print('Good bye!')
        quit()
    else:
        check()

