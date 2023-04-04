import random
import sys

def main():
    num = random.randint(1, 100)
    cnt = 0
    min = 1
    max = 100
    user = 0 # 사용자가 입력한 숫자
    size = 5 # 기회 횟수
    yn = "y","n"

    print("[맞는지 확인용 {}]" .format(num))
    print("자! 게임  시작해볼까요? \n시스템이 숫자를 선택했습니다.")

    for i in range(size, 0, -1) : #5회 기회를 주어 반복문 돌아갈 수록 1씩 감소
        cnt+=1
        user = int(input("{}번째. {}~{} 중 숫자 입력해주세요!({}회 남음)>> ".format(cnt, min, max, i)))

        while(user < min or user > max or user > 100 or user < 0):
            user = int(input("잘못입력하셨습니다! {}~{} 중 숫자 입력해주세요!({}회 남음)>> ".format(min, max, i)))

        if user < num :
            if i == 1 : #1회 기회 남은 상태에서 오답시 메시지 출력
                print("아쉽네요! 게임 종료되셨습니다. 정답은 '{}'입니다." .format(num), end='\n\n')
            else :
                print("UP!")
                min = user+1 # 입력한 숫자에서 1 증가
        elif user > num :
            if i == 1 : #1회 기회 남은 상태에서 오답시 메시지 출력
                print("아쉽네요! 게임 종료되셨습니다. 정답은 '{}'입니다." .format(num), end='\n\n')
            else :
                print("DOWN!")
                max = user-1 # 입력한 숫자에서 1 감소
        elif user == num :
            print("Good job!"*3, end='\n\n')
            break    

    choose = input("다시하시겠습니까(y/n)>> ")

    while not(choose in yn) :
        choose = input("잘못입력하셨습니다. 다시 입력해주세요(y/n)>> ")
    if choose == "n" :
        print("아쉽네요! 계속하자구!! 게임 종료되셨습니다.")
        sys.exit()
    elif choose == "y" :
        main()
        
main()