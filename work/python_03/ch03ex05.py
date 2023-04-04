numberA = input("첫번째 숫자를 입력하세요")
numberB = input("두번째 숫자를 입력하세요")
numberC = input("셋번째 숫자를 입력하세요")

sum = int(numberA + numberB + numberC)

print("입력하신 숫자는 %s, %s, %s 입니다." %(numberA, numberB, numberC))
print(str(numberA)+ "+"+str(numberB)+ "+" +str(numberC)+ "=" +str(sum))

maximun = max(str(numberA + numberB + numberC))
print(f"{numberA}, {numberB}, {numberC} 중 큰 수는 {maximun}입니다.")