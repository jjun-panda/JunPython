print("3개의 정수를 입력받아서 가장 큰 수와 가장 작은 수를 구하는 프로그램")

fir = int(input("첫번째 정수 입력>> "))
sec = int(input("두번째 정수 입력>> "))
thi = int(input("세번째 정수 입력>> "))

maxNum = max(fir, sec, thi)
minNum = min(fir, sec, thi)

print("{:-^30}".format("입력 결과"))
print("가장 큰 수는 %d입니다." %(maxNum))
print("가장 작은 수는 %d입니다." %(minNum))