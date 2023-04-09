# 선택 정렬 연습
# 선택정렬, 삽입정렬, 버블정렬

numList = [9,8,4,7,4,1,0,2,4,6,3,4,5]
newList = [0,0,0,0,0,0,0,0,0,0,0,0,0]
# 정렬되도록 출력하라
# for문을 이용해 볼 것
i = 0
for i in range(len(numList)-1):
    j = i+1
    print(i)
    # print(j)
    for j in range(i, len(numList)):
        print(j)
        if numList[j] < numList[i]:
            numList[i], numList[j] = numList[j], numList[i]
        j += 1
    i += 1
print(numList)

for i in range(0, len(newList)):
    m = min(numList)
    newList[i] = m
    numList.remove(m)

print(newList)
