import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=rub+to+eur&sxsrf=ALeKk01KIdQ1dfu0ISsvSU9hF7Todaq9JA%3A1618140454372&source=hp&ei=Jt1yYJDvFJ3kgweh2JaAAQ&iflsig=AINFCbYAAAAAYHLrNrU5R6FZH6Q4dJvqXqhj6pt0purh&oq=rub+to+e&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQywEQRhCCAjIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLAToECCMQJzoICC4QsQMQgwE6CAgAELEDEIMBOgsIABCxAxDHARCjAjoFCAAQsQM6DggAELEDEIMBEMcBEK8BOgIIADoFCC4QsQM6CAgAEMcBEK8BOgIILjoKCAAQsQMQRhCCAjoECAAQClDlJ1jXLWDkNWgAcAB4AIABywGIAYoHkgEFNC4zLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=gws-wiz'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

value = soup.find_all('span', {'class': "DFlfde SwHCTb"})
# # print(value.string)
# value = float(value.string.replace(',', '.'))
# # print(value)
# # print(type(value))
#
# user_amount = float(input("Please enter amount in RUB"))
# print(user_amount // value)

print(value.has_attr('namee'))

