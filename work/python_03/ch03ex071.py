import random


def game() :
    min = 1
    max = 100
    k = random.randint(1, 100)
    number = 0
    cnt = 0
    size = 5

    print(f"시스템이 숫자를 선택 했습니다. (힌트: {k})")

    while cnt < size :
        print(f"{cnt+1}/{size}번째 시도.")
        number = int(input(f"{min}~{max} 사이 입력: "))
        while not(number in range(min, max)) :
            print("범위를 초과 했습니다. 다시 입력하세요!")
            number = int(input(f"{min}~{max} 사이 입력: "))

        print(f"입력받은 번호는 {number}입니다.")
        if(k == number) :
            print("정답입니다.")
            break
        elif number > k :
            print("더 낮게")
            max = number - 1
        elif number < k :
            print("더 높게")
            min = number + 1

        cnt += 1

    if cnt == 5 :
        print("기회를 모두 소진 했습니다. 실격!")



while True :
    game()
    yn = input("계속 하시겠습니까?(y/n): ")
    if yn == "n" :
        break;

print("게임 종료!")