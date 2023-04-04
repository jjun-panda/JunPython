name = input("성명를 입력하세요")
email = input("이메일을 입력하세요")
phone = input("전화번호를 입력하세요")

print(f"성명: {name} | 이메일: {email} | 전화번호: {phone}")
print("당신의 이름은 %s이며, 이메일 주소는 %s이고, 연락처는 %s입니다." %(name, email, phone))
print("당신의 이름은 {}이며, 이메일 주소는 {}이고, 연락처는 {}입니다." .format(name, email, phone))