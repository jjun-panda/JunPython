# 파이썬 함수 선언 부
def main() :
    print("HEllo Python world");
    print(__name__)
    # 탭을 사용하면 함수 블럭 내부
    if False :
        print("이것은 if문 내부에서 출력한 것")

if __name__ == '__main__' :
    # 함수는 호출해야 실행한다.
    main()