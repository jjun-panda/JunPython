import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.jjuns-c.com")
assert response.status_code is 200
print(type(response.content))
print(type(response.text))

dom = BeautifulSoup(response.content, "html.parser")
print(type(dom))
print(dom.title)
print(dom.title.string)
print(type(dom.title))
print(type(dom.title.string))