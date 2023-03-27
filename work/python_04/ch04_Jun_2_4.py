while True:
    word = input('검색어입력>> ')
    if word == '그만' : break
    if len(word) < 3 :
        print("검색어가 너무 짧습니다.")
    elif len(word) >= 10 :
        print("검색어가 너무 깁니다.")
    else :
        print('입력받은 검색어는 '+word+'입니다.')

print('검색어 입력 프로그램을 종료 합니다.')