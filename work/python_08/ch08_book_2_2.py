fish_list = ['오징어', '꼴뚜기', '대구', '명태', '거북이']
print("생선을 주문하세요!")
for i, fish in enumerate(fish_list) :
    print(f"({i+1}) {fish} ", end="")

while True :
    try :        
        choice = int(input(">> "))
        print("-"*55)
        print(fish_list[choice - 1], end = "")
        break
    except IndexError as e:
        print(f"목록에 없는 번호 입니다. [{i-(i-1)}부터 {len(fish_list)}까지 입력해주세요!]")
    except ValueError as e:
        print(f"목록에 없는 번호 입니다. [{i-(i-1)}부터 {len(fish_list)}까지 입력해주세요!]")

print("주문완료")