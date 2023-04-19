import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.daum.net/")
assert response.status_code == 200

dom = BeautifulSoup(response.content, "html.parser")

search_list = dom.select("ul.list_newsissue")
# print(search_list)
a_list = search_list[0].find_all('strong', class_='tit_g')
for i, element in enumerate(a_list):
    print(i, element.find('a').text.strip())