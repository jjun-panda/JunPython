numList = [9,8,4,7,4,1,0,2,4,6,3,4,5]
newList = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(numList)):
    for j in range(i+1, len(numList)):
        if numList[j] < numList[i] :
            numList[j], numList[i] = numList[i], numList[j]


print(numList)
