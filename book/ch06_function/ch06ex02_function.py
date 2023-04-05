# 함수를 사용하는 이유
# 함수를 선언 해 두면 여러지점에서 반복 호출이 가능하다.
# 지금까지 사용한 print()나 input()도 함수의 일종이다.

def my_func() :
    print(">>> 함수를 호출 하였습니다!")
    print(">>> 이것은 함수 내부에 선언된 내용입니다!")


print("[1] 함수 외부에서 출력하였습니다.")
#함수 호출
my_func()
print("[2] 함수 외부에서 출력하였습니다.")
#함수 호출
my_func()
print("[3] 함수 외부에서 출력하였습니다.")
#함수 호출
my_func()
print("[4] 함수 외부에서 출력하였습니다.")


# 함수를 호출 하는것은 반복문을 사용하는것과는 다르다.
# 반복문이 실행 되는것은 소스코드의 한곳에서 여러번 실행 하는것이다.
# 한번 선언된 함수는 소스 코드의 여로곳에서 호출이 가능하다.
# 함수는 인수와 반환값을 가지며 이를 다양하게 활용 가능하다.