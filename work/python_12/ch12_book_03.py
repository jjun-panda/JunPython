import time
from SearchList import getSearchList

for cnt in range(20):
    search_list = getSearchList("https://news.daum.net/", "ul.list_newsissue")
    div_list = search_list[0].find_all('strong', class_='tit_g')
    for i, element in enumerate(div_list):
        print(i, element.find('a').text.strip())

    time.sleep(20)
    print("{:-^50}".format("20초 한번씩 검색"))



    