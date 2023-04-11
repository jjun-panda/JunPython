
# {
#     "o_seq" : 1,    # 주문고유번호
#     "o_name" : "",  # 주문상품명
#     "ea_price" : 0, # 개당 가격
#     "order" : [],   # 주문명
#     "count" : 0,    # 수량
# }
from datetime import datetime
import random

order_list = []
o_sequence = 1
product_list = [
	{"seq":1, "name":"에스프레소", "price":2000, "option":[{"step":1, "menu":[{"item":"HOT","opt_price":0}, {"item":"ICE","opt_price":500}]},{"step":2, "menu":[{"item":"텀블러 할인","opt_price":-300}, {"item":"할인 없음","opt_price":0}]},{"step":3, "menu":[{"item":"샷추가","opt_price":500}, {"item":"샷안함","opt_price":0}]}]},
	{"seq":2, "name":"과일음료", "price":4000, "option":[]},
	{"seq":3, "name":"아메리카노", "price":2000, "option":[{"step":1, "menu":[{"item":"HOT","opt_price":0}, {"item":"ICE","opt_price":500}]},{"step":2, "menu":[{"item":"텀블러 할인","opt_price":-300}, {"item":"할인 없음","opt_price":0}]},{"step":3, "menu":[{"item":"샷추가","opt_price":500}, {"item":"샷안함","opt_price":0}]}]},
	{"seq":4, "name":"카페라떼", "price":3000, "option":[{"step":1, "menu":[{"item":"HOT","opt_price":0}, {"item":"ICE","opt_price":500}]},{"step":2, "menu":[{"item":"텀블러 할인","opt_price":-300}, {"item":"할인 없음","opt_price":0}]},{"step":3, "menu":[{"item":"샷추가","opt_price":500}, {"item":"샷안함","opt_price":0}]}]},
]
sequence = 5

def menu_fn() :
	print("{:-^40}".format("MENU"))
	for i, product in enumerate(product_list) :
		print(f"{i+1}.{product['name']} ({product['price']}원)")
	no = int(input("선택>> "))
	while not(no > 0 and no <= len(product_list)) :
		print(f"1 ~ {len(product_list)} 사이의 번호를 입력해주세요")
		no = int(input("다시 입력>>"))
	return no

def order_fn():
	global o_sequence
	print("{::^40}".format("메머드 커피 주문"))
	no = menu_fn()
	idx = no -1

	order_dict = {
		"o_seq" : o_sequence,    # 주문고유번호
		"o_name" : product_list[idx]['name'],   # 주문명
		"o_option" : [],
		"ea_price" : product_list[idx]['price'], # 개당 가격
		"count" : 1    # 수량
	}
	order_list.append(order_dict)
	o_sequence += 1
	
	print(">>", order_dict['o_name'], "선택.")

	# 옵션 선택
	for opt_item in product_list[idx]['option'] :
		print(f"--------- {opt_item['step']}단계 옵션 선택")
		opt_list = opt_item['menu']
		for num, menu in enumerate( opt_list ) :
			print(f"{num+1}. {menu['item']} ({menu['opt_price']}원)")
		opt_no = int(input("선택: "))
		ppt_idx = opt_no-1
		order_dict['ea_price'] += opt_list[ppt_idx]['opt_price']
		order_dict['o_option'].append(opt_list[ppt_idx]['item'])

	ea = int(input("수량 선택>> "))
	order_dict["count"] = ea
	

def main() :
	while True :
		order_fn()
		print("{:-^30}".format("상품이 추가 되었습니다!"))
		print("{:-^30}".format("결제 / 추가 / 취소"))
		for order in order_list :
			print("선택상품: ", order['o_name'], order['o_option'], "*", order['count'], "잔.")
		print("1. 결제")
		print("2. 추가")
		print("3. 취소")
		no = int(input("선택: "))
		if no == 1 :
			break
		elif no == 2 :
			continue
		elif no == 3 :
			order_list.clear()  # 주문 지우고 취소
			return
		
	if len(order_list) > 0 :
		print("{:-^30}".format("결제 정보 입력"))
		print(">>선택상품")
		total_price = 0
		for i, order in enumerate(order_list) :
			total_price += order['ea_price'] * order['count']
			print(f"[{i+1}]", order["o_name"], order["o_option"], "*", order["count"])

		print("결제금액: ", total_price )
		print("카드번호 입력: 413720*****")
		print("{:-^30}".format("결제 완료"))
		print()

		print("{:-^30}".format("^_^ 우리가 사랑하는 널 응원해"))
		print("{:-^30}".format("[영수증]"))
		print("매장")
		number = random.randint(1,500)
		print("교환권 번호: ", number)
		print("매머드 커피")
		print("3480401419 / 최혜원 / TEL False")
		order_number = random.randint(000,999)
		current_time = datetime.now()
		timeSrt = current_time.strftime("%Y-%m-%d %H:%M:%S")
		yearSrt = current_time.strftime("%Y")
		print(f"주문번호: {yearSrt}{order_number}")
		print(f"주문일자: {timeSrt}")
		print("="*30)
		print("{: <15}{: <6}{: <6}".format("상품명", "수량","금액"))
		print("-"*30)
		for order in order_list :
			print("{: <15}{: <6}{: <6}".format(order['o_name'], order['count'], order['ea_price']))
			for opt_item in order['o_option'] :
				print("-", opt_item)
		print("="*30)
		vatA = total_price*10/11
		vatB = total_price-vatA
		print("{: <22}{: <6}".format("공급가액", int(vatA)))
		print("{: <24}{: <6}".format("부가세", int(vatB)))
		print("="*30)
		print("신용카드")
		print("승인금액:", total_price)
		print("승인일자: 20230411073514")
		print("카드사: 삼성비자카드")


if __name__ == "__main__":
	main()