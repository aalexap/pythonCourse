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

pattern = re.compile(r'\nabc')

# matches = pattern.findall(text_to_search)
# print(matches)

# print(re.findall(r'\d\d\d', text_to_search))

matches = pattern.fullmatch('\nabc')
print(matches)
