import requests
from requests.exceptions import HTTPError

# 200 - success
# 300 - redirect
# 400 - client errors
# 500 - server errors

r = requests.get('https://xkcd.com/353/', timeout=3)

print(r)
# print(r.text)  # - html code
print(r.content)  # байтовая строка
print(r.status_code)
print(r.ok)
print(r.headers)
print(r.headers['server'])
print(r.encoding)
print(r.cookies)


# pic = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=3)
# with open ('comic.png', 'wb') as file:
#     file.write(pic.content)

for url in ['https://api.github.com', 'htpps://api.githum.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('Success')