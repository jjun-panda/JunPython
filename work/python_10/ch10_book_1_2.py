# 파일을 읽기 모드로 열기
fp = open("test.text", "r", encoding="utf-8")

# 파일에 내용 읽기
lines = fp.readlines()
for line in lines:
    print(line, end="")

fp.close()
print("-"*30)