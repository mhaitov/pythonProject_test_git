import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
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
Mrs. Robinson-Asd
Mr. T
abc


Mall, Hall, Wall, Tall
'''


# sentence = 'Start a sentence and then bring it to an end'
#
# # pattern = re.compile(r'\bHa')
# # pattern = re.compile(r'\BHa')
# #
# # pattern = re.compile(r'^start')
# # pattern = re.compile(r'end$')
# # pattern = re.compile(r'sentence$')
#
# ## Dlja nomerov
# # pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# # pattern = re.compile(r'\d\d\d[-\.]\d\d\d[-\.]\d\d\d\d')
# # pattern = re.compile(r'[89]00[-\.]\d\d\d[-\.]\d\d\d\d')
# # pattern = re.compile(r'[89]00[-\.]\d{3}[-\.]\d{4}')
# # pattern =  re.compile(r'\d{3,4}')
# # pattern =  re.compile(r'\d{3,4}[^0-9]')
# # pattern = re.compile(r'[a-z]')
#
# #### ^ - Dont found word
# # pattern = re.compile(r'[^Ww]all')
#
#
#
# # pattern = re.compile(r'[A-Za-z]')
#
# #
# # print('\tTab')
# # #### Syraja stroka, ne raspoznaet simvoly
# # print(r'\tTab')
#
# # pattern = re.compile(r'example.com')
# # # pattern = re.compile(r'example\.com')
#
# # pattern = re.compile(r'M[rs]')
# pattern = re.compile(r'M(rs|r|s)\.? [A-Z][A-Za-z-]*')
#
#
#
# matches = pattern.finditer(text_to_search)
# # matches = pattern.finditer(sentence)
# # # print(matches)
# #
# # # for match in matches:
# # #     print(match)
# # #
# # # print(text_to_search[1:4])
# # # print(text_to_search[264:267])
#
#
#
# for match in matches:
#     print(match.start()), match.end(), match.group()
#
# with open('people.txt', 'r', encoding='utf8') as file:
#     people_data = file.read()
#
#     pattern = re.compile(file.read(r'\d{3}--\d{3}--\d{4}'):
#     matches = pattern.finditer(people_data)
#
# for match in matches:
#     print(match.group)
########################################


emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net

# '''
#
# #### FORMULA POISKA EMAIL
# # pattern = re.compile(r'[A-Za-z0-9-\._+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z]+')
# # pattern = re.compile(r'[A-Za-z0-9-\._+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(\.[a-zA-Z]+)')
# #
# # matches = pattern.finditer(emails)
#
#
# # pattern = re.compile(r'(https*://)?(www\.)?(\w)+(\.[a-zA-Z]+)')
# #
# # matches = pattern.finditer(urls)
# #
# # subbed.urls = pattern.sub(r'1\2\3\4', urls)
# # print(subbed_urls)
# #
# #
# # for match in matches:
# # #     # print(match)
# # #     # print(match.group(0))
# # #     # print(match.group(1))
# # #     # print(match.group(2))
# # #     # print(match.group(3))
# #     print(match.group(3) + match.group(4))
#
# #####################################
#
# sentence = 'Start a sentence and then bring it to an end\nStart'
#
# # pattern = re.compile(r'M(rs|r|s)\.?[A-Z[a-z]*')
# # pattern = re.compile(r'(\d{3})\.(\d{3}\.\d{4})')
# # pattern = re.compile(r'\d{3}\.d{3}\.d{4}')
# pattern = re.compile(r'sentance')
# #
# # finder = pattern.match(text_to_search)
# # finder = pattern.search(text_to_search)
# # print(finder)
# # #
#
# finder = pattern


# pattern = re.compile(r'ESCAped',re.IGNORECASE)
# pattern = re.compile(r'^\d', re.M)
pattern = re.compile(r'', re.DOTALL)


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)