# 상수처럼 사용될 변수 선언
# 모두 대문자로 선언, 나중에 수정하고자 하면 경고 메시지를 보여줌
CONST_DATA = '수정 할 수 없는 데이터 입니다!'
CINST_NUMBER = 365

# 클래스 선언 시에는 메소드에 @constant 키워드를 붙어서 getattr로 지정
# setter로 지정되면 이 메소드를 이용해서 값 변경이 불가능
class ConstTest :
    def __init__(self) :
        self._name = 'const_test'

        @constant
        def getData(self) :
            return self._name