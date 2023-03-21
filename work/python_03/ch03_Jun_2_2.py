text = input("문자열 입력>> ")
old = input("찾을 단어>> ")
new = input("바꿀 단어>> ")
start = text.index(old)
end = start + len(old)

result = text[:start] + new + text[end:]

print("{:-^14}".format("결과"))
print(result)