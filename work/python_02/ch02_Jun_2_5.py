print("이름, 이메일, 전화번호, 주소를 입력받는 프로그램")

name = input("이름 입력>> ")
mail = input("이메일 입력>> ")
call = input("전화번호 입력>> ")
addr = input("주소 입력>> ")

print("{:-^70}".format("입력 결과"))
print("%-10s %-20s %-20s %-20s" %("name", "email", "phone", "address"))
print("%-10s %-20s %-20s %-20s" %(name, mail, call, addr))