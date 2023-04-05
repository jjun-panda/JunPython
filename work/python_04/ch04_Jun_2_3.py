word = input('검색어입력>> ')
if len(word) < 3 :
    print("검색어가 너무 짧습니다.")
elif len(word) >= 10 :
    print("검색어가 너무 깁니다.")
else :
    print("입력받은 검색어는 "+word+"입니다.")