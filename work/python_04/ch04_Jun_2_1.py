print("금액을 입력받아서 돈의 종류별 개수를 환산하는 프로그램")

total = int(input("금액 입력>> "))
money = total
w50000 = money // 50000
money = money % 50000
w10000 = money // 10000
money = money % 10000
w5000 = money // 5000
money = money % 5000
w1000 = money // 1000
money = money % 1000
w500 = money // 500
money = money % 500
w100 = money // 100
money = money % 100
w50 = money // 50
money = money % 50
w10 = money // 10
money = money % 10
w5 = money // 5
money = money % 5
w1 = money;

print("{:-^14}".format("결과"))
print("오만원권 : {}" .format(w50000))
print("만원권 : {}" .format(w10000))
print("오천원권 : {}" .format(w5000))
print("천원권 : {}" .format(w1000))
print("오백원 : {}" .format(w500))
print("백원 : {}" .format(w100))
print("오십원 : {}" .format(w50))
print("십원 : {}" .format(w10))
print("오원 : {}" .format(w5))
print("일원 : {}" .format(w1))