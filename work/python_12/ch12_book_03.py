# # daum
# import time
# from SearchList import getSearchList

# for cnt in range(20):
#     search_list = getSearchList("https://news.daum.net/", "ul.list_newsissue")
#     div_list = search_list[0].find_all('strong', class_='tit_g')
#     for i, element in enumerate(div_list):
#         print(i, element.find('a').text.strip())

#     time.sleep(20)
#     print("{:-^50}".format("20초 한번씩 검색"))


# # yahoo_jp
# import time
# from SearchList import getSearchList

# for cnt in range(20):
#     search_list = getSearchList("https://news.yahoo.co.jp/topics", "div.sc-hzUIXc.jSTRnN")
#     print(search_list)
#     div_list = search_list[0].find_all('li', class_='sc-fHCHyC jhKFuK')
#     for i, element in enumerate(div_list):
#         print(i, element.find('a').text.strip())

#     time.sleep(20)
#     print("{:-^50}".format("20초 한번씩 검색"))

# # 연합뉴스
# import time
# from SearchList import getSearchList

# for cnt in range(20):
#     search_list = getSearchList("https://yonhapnewstv.co.kr/news/headline", "div.cont-item01")
#     # print(search_list)
#     div_list = search_list[0].find_all('div', class_='item-body')
#     for i, element in enumerate(div_list):
#         print(i, element.find('a').text.strip())

#     time.sleep(20)
#     print("{:-^50}".format("20초 한번씩 검색"))

# # hani
# import time
# from SearchList import getSearchList

# for cnt in range(20):
#     search_list = getSearchList("https://www.hani.co.kr/arti/list.html", "div.section-list-area")
#     print(search_list)
#     div_list = search_list[0].find_all('h4', class_='article-title')
#     for i, element in enumerate(div_list):
#         print(i, element.find('a').text.strip())

#     time.sleep(20)
#     print("{:-^50}".format("20초 한번씩 검색"))


# 다음뉴스_사회
import time
from SearchList import getSearchList

for cnt in range(20):
    search_list = getSearchList("https://news.daum.net/breakingnews/society", "div.box_etc")
    print(search_list)

    div_list = search_list[0].find_all('strong', class_='tit_thumb')
    print(div_list)

    for i, element in enumerate(div_list):
        print(i, element.find('a').text.strip())

    time.sleep(20)
    print("{:-^50}".format("20초 한번씩 검색"))
