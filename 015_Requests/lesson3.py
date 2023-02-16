import requests
from bs4 import BeautifulSoup as BS

eur_to_yen = 'https://www.google.com/search?q=eur+to+yen&client=firefox-b-d&sxsrf=AJOqlzUUzctNUsnw73N9NuNbdE9W2BQtBQ%3A1676569013414&ei=tWnuY73oGPGExc8Pu9e6aA&ved=0ahUKEwj9lvGjypr9AhVxQvEDHburDg0Q4dUDCA4&uact=5&oq=eur+to+yen&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzINCAAQgAQQywEQRhCCAjIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCwgAEBYQHhDxBBAKMgkIABAWEB4Q8QQ6CggAEEcQ1gQQsAM6BAgjECc6BAgAEEM6CwgAEIAEELEDEIMBOgoIABCxAxCDARBDOgoILhCxAxCDARBDOggIABCABBCxAzoQCAAQgAQQFBCHAhCxAxCDAToJCAAQQxBGEIICOg0IABCABBCxAxCDARAKOgcIABCABBAKOgYIABAWEB5KBAhBGABQpQJYwRhg_BpoAXABeAGAAeEEiAGsD5IBBzAuOS41LTGYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

full_page = requests.get(eur_to_yen, headers=headers)
soup = BS(full_page.content, 'html.parser')

rate = soup.find('span', class_='DFlfde SwHCTb')
# print(float(rate.text.replace(',', '.')))
rate = float(rate['data-value'])

user_amount = float(input('Please enter amount of eur:'))
print(user_amount * rate)