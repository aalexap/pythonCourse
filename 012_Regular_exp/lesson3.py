import re

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
example@mysite.company.com
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

# pattern = re.compile(r'[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-ZaZ0-9-.]+')
# pattern = re.compile(r'[\w.-]+@([\w-]+\.)+[\w-]{2,4}')
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)

pattern = re.compile(r'(http://|https://)?(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3) + match.group(4))

print(re.sub(r'example', 'sample', urls))