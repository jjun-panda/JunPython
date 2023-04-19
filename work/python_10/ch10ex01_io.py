# 파일 생성
fp = open("io.tset.text", "w")

# 파일에 내용 쓰기
fp.write("I can do!")

# 사용자 입력
str = input("입력해주세요 >> ")
fp.write(str)

# 열려진 파일 닫기
fp.close()