# 파일 생성
fp = open("jjun.text", "a")

# 파일에 내용 출력

# 사용자 입력
str = input("당신의 이릅은 >> ")
fp.write(str+ "\n")
str1 = input("당신의 거주지는 >> ")
fp.write(str1+ "\n")
str2 = input("당신의 직업은 >> ")
fp.write(str2+ "\n")
str3 = input("당신의 소속은 >> ")
fp.write(str3+ "\n")

# 열려진 파일 닫기
fp.close()