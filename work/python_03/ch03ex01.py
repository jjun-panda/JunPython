name = "홍길동"
age = 30

print(name, "님은 3살만 어려진다면,", age-3, "세 입니다.", sep="", end="\n")
print("%s님은 3살만 어려진다면, %d세 입니다." %(name, age-3))
print("{}님은 3살만 어려진다면, {}세 입니다." .format(name, age-3))
print(f"{name}님은 3살만 어려진다면, {age-3}세 입니다.")

# 여러줄 문자열(따옴표 3개)
infoData = """
이것은 여러줄 문자열
주소: {}\n
전화번호: {}
""".format("서울시 강남구", "010-1234-5678")

print(infoData)

sql = """
insert into saram
values({},{},{})
""".format("Kim", "김코딩", 30)

print(sql)