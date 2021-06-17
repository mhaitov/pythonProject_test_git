import requests
from bs4 import BeautifulSoup
# #
# # html = '<p id="this is id" class="multi class attribute"><a rel="index">Hello world</a></p>'
# # # soup = BeautifulSoup(html, 'html.parser')
# # soup = BeautifulSoup(html, 'html.parser', multi_valued_attributes=None)
# # #
# # # print(soup.p['id'])
# # # print(soup.p['class'])
# # # #
# # # # print(soup.a['rel'])
# # # # soup.a['rel'] = ['rel', 'contents']
# # # # print(soup.a['rel'])
# # # soup.a['rel'] = ['index', 'contents']
# # # print(soup.a['rel'])
# #
# # ####### poluchenie atributov v vide spiska
# # print(soup.p.get_attribute_list('id'))
# # print(soup.p.get_attribute_list('p'))
#
# #####################################################3
# #
# # soup_footer = BeautifulSoup('<document><content/>INSERT FOOTER HERE</document>', 'xml')
# # footer = BeautifulSoup('<footer>I AM NEW FOOTER</footer>', 'xml')
# # print(soup_footer.text)
# # soup_footer.find(text="INSERT FOOTER HERE").replace_with(footer)
# # print(soup_footer.text)
# # print(soup_footer)
# #
# #
# #
# r = requests.get('https://www.google.com')
# r_soup = BeautifulSoup(r.content, 'html.parser')
# #
# # # print(r_soup.head)
# # # print(r_soup.body)
# #
# # print(r_soup.body.b)
#
# head_tag = r_soup.head
# # print(head_tag.contents)
# # print(head_tag.contents[2])
# title_tag = head_tag.contents[2]
# # # print(title_tag)
# #
# # # ########### DESENDANTS all tags in main
# # # for child in head_tag.descendants:
# # #     print(child)?
# # #
# # #
# # # print(title_tag.parent)
# #
# # print(title_tag.text)
# # print(title_tag.string)
# # print(title_tag.contents)
#

sibling_soup = BeautifulSoup('<a><b>Hello</b><c>World</c></a>', 'html.parser')
# # # print(sibling_soup)
# # # print(sibling_soup.prettify())
# # print(sibling_soup.b.next_sibling)
# # print(sibling_soup.c.previous_sibling)
#
#
# for sibling in sibling_soup.b.next_siblings:
#     print(sibling)
#
# for sibling in sibling_soup.c.previous_siblings:
#     print(sibling)
#

r = requests.get('https://www.google.com')
r_soup = BeautifulSoup(r.content, 'html.parser')

# print(r_soup.find_all(class_='gb1'))

# print(r_soup.find_all(href="https://news.google.com/?tab=wn"))

soup_match = r_soup.find_all(attrs={'class': 'gb1', 'href': True}, limit=4)
for x in soup_match:
    print(x)

