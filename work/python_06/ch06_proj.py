import random

foodList = [
	{"seq":1, "title":"라돈모다기", "money":9500},
	{"seq":2, "title":"비빔모다기", "money":9500},
	{"seq":3, "title":"미니탕수육", "money":3500},
	{"seq":4, "title":"만두육개장", "money":9000},
	{"seq":5, "title":"로제떡볶이", "money":5500},
	{"seq":6, "title":"등심돈까스", "money":7500},
	{"seq":7, "title":"순두부찌개", "money":7000},
]

order = {}

def food():
	menuList()
	user()
	pay_order(order)

def menuList():
	print("{:-^30}".format(" 메뉴 "))
	for i in foodList:
		print("{}. {:<10} {:>6}원".format(i['seq'], i['title'], i['money']))

def add_order(order, food_num, count):
	if food_num in order:
		order[food_num] += count
	else:
		order[food_num] = count

def user():
	num = int(input("메뉴 번호를 입력해주세요>> "))
	while True:
		for i in foodList:
			if num == i['seq']:
				food_num = i['seq']
				count = int(input("개수를 입력해주세요>> "))
				add_order(order, food_num, count)
				print("-"*20, "\n>> 현재 주문 내역 ")
				for food_num, count in order.items():
					for food in foodList:
						if food['seq'] == food_num:
							print("  ", food['title'], count)
				print("-"*20, "\n")

				order_add = input("추가 주문하시겠습니까?(Y/N)>> ")
				while not (order_add in["y","n"]) :
					print("y 또는 n 만 입력해주세요!")
					order_add = input(">>추가 주문하시겠습니까?(Y/N)")
				if order_add == "y":
					print("\n"+"*"*30)
					user()
					return
				elif order_add == "n":
					return
				return
		if num != i['seq']:
			print(">>앗! 해당 메뉴는 없습니다.")
			num = int(input("다시 입력해주세요>> "))


def pay_order(order):
	total = 0
	for food_num, count in order.items():
		for food in foodList:
			if food['seq'] == food_num:
				total += food['money'] * count
	print(f"총 금액은 {total}원 입니다.")

	userPay = int(input("결제 금액을 입력하세요: "))

	while True:
		if userPay >= total:
			change = userPay - total
			print(f"거스름돈은 {change}원입니다")
			end = input("영수증 발행하시겠습니까?(Y/N)>> ")
			if end == "y" :
				printBill(order, total, userPay, change)
			elif end == "n" :
				print("맛있게 드세요!")
			break
		else :
			print("결제 금액이 부족합니다.")
			userPay = int(input("다시 결제해주세요>> "))

# 영수증 발행
def printBill(order, total, userPay, change):
	print("\n{: ^37}".format("[영수증]"))
	number = random.randint(1,500)
	print(f"주문번호: {number}")
	print("="*40)
	print("{:<12}{:^6}{:^5}{:^10}".format("상품명","단가","수량","금액"))
	print("-"*40)
	for food_num, count in order.items():
		for food in foodList:
			if food['seq'] == food_num:
				print("{:<10}{:^8}{:^5}{:>10}".format(food['title'], food['money'], count, food['money']*count))
	print("="*40)

	vatA = int(total*10/11)
	vatB = total - vatA
	print("{:<23}{:>6}".format("부가세 과세 물품가액 :", vatA))
	print("{:<23}{:>12}".format("부       가       세 :", vatB))
	print("-"*40)
	print("{:<23}{:>13}".format("합    계 :", total))
	print("{:<23}{:>11}".format("받을금액 :", total))
	print("{:<23}{:>11}".format("받은금액 :", userPay))
	print("{:<23}{:>11}".format("거스름돈 :", change))
	print("-"*40)
	print("{: ^29}".format("맛있게 드시고 건강하세요!"))
	return

if __name__ == "__main__":
	food()
