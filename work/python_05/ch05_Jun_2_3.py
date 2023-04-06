import random


lis = list(range(1,17))
random.shuffle(lis)

new_lis = []
cnt = 0
for i in range(4) :
	new_lis.append([])
	for j in range(4) : 
		new_lis[i].append(lis[cnt]) 
		cnt += 1
print(new_lis, indent=2, width=20)