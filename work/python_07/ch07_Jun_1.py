# 1안
total = 0
num = 10
a = 1
b = 1

def fibo(i):
	global a, b, total, num

	if i <= num :
		total += a
		print(str(a) + ("+" if i < num else ""), end="")
		c = a + b
		a= b
		b =c
		fibo(i+1)
	else :
		print("=", end="")
		return
fibo(1)
print(total)


# 2안
total = 0
num = 10
a = 0
b = 1
def fibo(i):
	
	for j in range(2, i+1):
		c = a + b
		a= b
		b =c
	return b

for i in range(1, num+1):
	total += fibo(i)
	print(str(fibo(i)) + "+" if i < num else str(fibo(i)) + "=", end="")
print(total)