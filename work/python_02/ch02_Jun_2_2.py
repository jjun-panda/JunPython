import math
print("원의 둘레와 넓이를 구하는 프로그램")

PI = math.pi
r = int(input("원의 반지름 입력>> "))
# 둘레길이 = 반지름*2*파이
line = 2 * PI * r

# 넓이 = 반지름*반지름*파이
area = PI * r * r

print("반지름이 {}인 원 둘레의 길이는 {}이고 넓이는 {}입니다." .format(r, line, area))
print("반지름이 %d인 원 둘레의 길이는 %.4f이고 넓이는 %.4f입니다." %(r, line, area))