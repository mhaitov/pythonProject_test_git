import requests

####### Metody primenjaemye k zaprosu v brauzere
r = requests.get('https://xksd.com/353/', timeout=5)

print(r)

# 200 - succes
# 300 - redirect
# 400 - client errors
# 500 - server errors


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
r = requests.get('https://xksd.com/353/', headers=headers, timeout=5)
# print(r)
# print(r.status_code)
# print(r.text)
# print(r.content)
image = requests.get()
with open('comic.png', 'web') as image_file:
    image_file.write(image.content)

print(r.headers)
print(r.next)
print(r.text)
print(r.json())

print(r.url)
