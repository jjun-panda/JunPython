# 함수선언
def print_hi(name):
    print(f'Hi, {name}')
    print(__name__, "의 실행 print_hi 완료")

# 만약 현재 파일에서 직접 실행하면 실행된다.
# 다른 파일에서 현재파일을 모듈로 import하면 즉시 실행되지 않음
# 다른 파일에서 현재파일을 모듈로 import 할 때 자동 실행되는 것을 방지한다
if __name__ == '__main__':
    print("111111")
    # 함수 호출
    print_hi('Python')

    print("실행 완료")