name = input("이름 입력>> ")

while True:
    try :
        age = int(input("나이 입력>> "))
        break
        
    except ValueError :
        print("숫자만 입력해주세요!")
        continue

print(name + "님은 ", end="")
if age < 19 :
    print("미성년자 입니다.")
elif age < 35 :
    print("청년입니다.")
elif age < 65 :
    print("중년입니다.")
else :
    print("노년입니다.")
