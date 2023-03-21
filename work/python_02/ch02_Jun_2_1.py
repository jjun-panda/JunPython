print("성적 출력 프로그램입니다.")

name = input("성명 입력>> ")
kr = int(input("국어 성적 >> "))
eg = int(input("영어 성적 >> "))
mt = int(input("수학 성적 >> "))

total = kr + eg + mt
avg = total // 3.0;

print("{:-^30}".format("계산 결과"))
print("성명 : " + name)
print("국어 : " + str(kr))
print("영어 : " + str(eg))
print("수학 : " + str(mt))
print("총점 : " + str(total))
print("평균 : " + str(avg))
