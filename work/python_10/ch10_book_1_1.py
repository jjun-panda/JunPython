# 파일을 쓰기 모드로 열기
fp = open("test.text", "w", encoding="utf-8")

# 파일에 내용 쓰기
fp.write("Hello World\n")

# 파일 닫기
fp.close()