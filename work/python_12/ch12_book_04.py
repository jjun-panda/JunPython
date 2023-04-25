import requests
from SearchList import getSearchList
import pickle

search_list = getSearchList("https://news.daum.net/", "ul.list_newsissue")
div_list = search_list[0].find_all('strong', class_='tit_g')
imgList = []

for i, element in enumerate(div_list):
    imgTags = getSearchList("https://news.daum.net" + element.find("a")["href"], "img.thumb_g")

    images = []
    for j, img in enumerate(imgTags) :
        src = img.get("src")
        response = requests.get(src[:src.index("?")])

        if response.status_code == 200:
            ext = src.split(".")[-1]
            imgUrl = f"newImg{i}{j}.{ext}"
            images.append(f"./news/{imgUrl}")

            with open(f"news/{imgUrl}", "wb") as fp :
                fp.write(response.content)

    imgList.append(images)

with open("news/imgList.txt", "wb") as fp :
    pickle.dump(imgList, fp)
