import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
mall hall wall tall ball
sell xall fall 
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern =re.compile(r'[a-ftxs]all')

pattern = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*\b')

matches = pattern.finditer(text_to_search)

for match in matches:
    # print(match.start())
    # print(match.end())
    # print(match.group())
    print(match)
