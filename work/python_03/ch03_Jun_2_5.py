peoNum = input("주민 번호를 -를 포함해서 입력하라>> ")
fullNum = peoNum.index('-')
leftNum = peoNum[:fullNum]
rightNum = peoNum[fullNum+1:]
print("주민번호 앞자리 : " + leftNum)
print("주민 번호 뒷 첫글자 : " + rightNum[0])