# 여러행 문자열의 모양은 여러줄 주석의 모양과 동일하다.
# 여러행 문자열도 format함수로 가공 할 수 있다.

multiline = '''여러행의 문자열
우리나라는 {}이다.
서기 {}년{}월{}일'''.format("대한민국",2018,4,15)
print(multiline)

# 파이썬에서는 문자열(string)과 문자(charator)의 구분이 없다.
# 문자열 문자 모두 '' 또는 ""로 표현.