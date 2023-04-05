# 함수를 호출할때 함수로 데이터 전달이 가능하다.
# 함수로 전달 되는 데이터를 인수라 하고
# 인수를 받기위해 함수에 선언하는 변수를 매개 변수라 한다.
# 인수른 argument라고도 한다.

'''
# 함수를 선언할때 매개변수를 함께 선언 가능하다.
# 매개변수는 함수로 전달된 인수를 저장하기 위한 변수이다.
def 함수(매개변수) :
    함수의 몸체


함수를 호출할때 인수를 전달 할수 있다.
함수(인수)
'''

# 함수의 매개변수는 1개 이상 여러개를 선언할 수있고
# 홈수를 호출 할때는 매개변수의 갯수만큼 인수를 전달 해야 한다.
# 키워드 인수를 쓰지 않는이상
# 인수는 함수에 선언된 매개변수의 순서대로 함수로 전달 된다.

# 숫자인 인수를 전달 받아 출력하는 함수
def show_number(num) :
    print("[1] 함수로 전달된 숫자는 ", num, "입니다", sep="")


# 함수를 호출 할때 인수를 전달 한다.
show_number(5)