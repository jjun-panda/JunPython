import random
import sys


def main() :
    min = 1
    max = 100
    k = random.randint(1,100)
    number = 0
    cnt = 1 #횟수
    size =5 #기회
    yn = "y","n"
    print(f"시스템이 숫자를 선택 했습니다. 입력 기회는{size}회 (이스터에그: {k})")
    number = int(input(f"{cnt}>>{min}-{max} 사이 입력: "))
    cnt = 2
    while True :
        size -= 1
        if number<k :
            if size < 1:
                print("기회를 다 사용하였습니다")
                anser = input("다시하시겠습니까?")
                while not (anser in yn):
                    print("문자가 안맞습니다")
                    anser = input("다시입력하세요: ")
                if anser == 'y':
                    main()

                elif anser == 'n':
                    print("프로그램을 종료합니다.")
                    sys.exit()
            print(f"더 높게 (기회{size}회 남음)")
            if min<number:
                min = number
            else: min
            number = int(input(f"{cnt}>>{min}-{max} 사이 입력: "))
            cnt += 1

        elif number>k :
            if size < 1:
                print("기회를 다 사용하였습니다")
                anser = input("다시하시겠습니까?")
                while not (anser in yn):
                    print("문자가 안맞습니다")
                    anser = input("다시입력하세요: ")
                if anser == 'y':
                    main()

                elif anser == 'n':
                    print("프로그램을 종료합니다.")
                    sys.exit()
            print(f"더 낮게 (기회{size}회 남음)")
            if max>number:
                max = number
            else: max
            number = int(input(f"{cnt}>>{min}-{max} 사이 입력: "))
            cnt += 1

        elif number==k :
            anser = input("맞았습니다.\n다시하시겠습니까?")
            while not(anser in yn) :
                print("문자가 안맞습니다")
                anser = input("다시입력하세요: ")
            if anser == 'y' :
                main()

            elif anser == 'n':
                print("프로그램을 종료합니다.")
                sys.exit()


main()