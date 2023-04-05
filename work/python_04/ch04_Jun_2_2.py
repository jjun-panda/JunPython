cityName = input("사는 도시 입력>> ")
if cityName in ['서울', '세종'] :
    print(cityName +'는 특별시 입니다.')
elif cityName in ['대전','대구','부산','광주','울산','인천'] :
    print(cityName + '는 광역시입니다')
else :
    print(cityName + '는 특별시나 광역시가 아닙니다')    