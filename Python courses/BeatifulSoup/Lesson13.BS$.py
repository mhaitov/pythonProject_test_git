import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com')
# print(r)

# soup = BeautifulSoup(r.content, 'html.parser')

# # print(soup)
# # print(soup.prett)
# # printify())
# print(soup.title(soup.title.string)
# print(soup.title.text)
# # print(soup.title.parent)
# # print(soup.title.parent.name)
#
#
# #
# # print(soup.p)
# # print(soup.p['style'])
# #
# # ###### LINK
# # print(soup.a)

# ####### href - eto sylka (in teg 'A')
# # print(soup.find_all('a'))
# # for link in soup.find_all('a'):
# #     print(link)
# # ###### OR
# # for link in soup.find_all('a'):
# #     print(link.text, link['href'])
#
# for link in soup.find_all('a'):
#     print(link['href'])
#
#
# print(soup.find(id='gbar'))
# print(soup.find(class_="gb1"))
# print(soup.find('div'))
#

# print(soup.get_text())

soup = BeautifulSoup('<b class="boldest">Extremly bold</b>', 'html.parser')
# print(soup)
# tag = soup.b
# print(type(tag))
# print(type(tag.name))
tag = soup.b

tag['id'] = 'verybold'
tag['another-attribute'] = 1
print(tag)

########## DELETE
del tag['id']
del tag['another-attribute']
print(tag)
