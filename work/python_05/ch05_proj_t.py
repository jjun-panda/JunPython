import sys

tList = [
	{"seq":1, "title":"친구 만나기", "done":True},
	{"seq":2, "title":"과제 하기", "done":False},
	{"seq":3, "title":"붕어 밥 주기", "done":False}
]
sequence = 4
select_todo = None


def print_row(item) :
	print("[{0}] ({1}){2}".format(item['seq'], "굳" if item['done'] else "놉", item['title']))

def print_list() :
	print("{:-^40}".format(" Todo List "))
	for i, item in enumerate(tList) :
		print_row(item)
		

def menu(menu_item) :
	for i, item in enumerate(menu_item) :
		if i == 0 :
			print("{:-^40}".format(f" {menu_item[0]} "))
		else :
			print(f"{i}.{menu_item[i]}", end = " ")
	
	no = int(input("\nCheck: "))
	while not no>0 and no<len(menu_item):
		print(f"입력오류: {1} ~ {menu_item - 1} 사이에만 입력해주세요")
		no = int(input("Check: "))
	return no
	
def insert_todo() :
	global sequence

	print("{:-^20}", " 할일 추가 ")
	tList.append({
        "seq": sequence,
        "title": input("새 할 일 입력>> "),
        "done": False
	})
	print("새 할 일 입력 완료!")
	sequence += 1

def modify01() :
	print("{:-^20}".format(" 상태 수정 "))
	select_todo['done'] = not(select_todo['done'])
	print_row(select_todo)


def modify02() :
	print("{:-^20}".format(" 할일 수정 "))
	select_todo['title'] = input("다시 입력해주세요.")
	print_row(select_todo)


modify_fn_factory = [None, modify01, modify02]

def modify_todo() :
	global select_todo

	seq  = int(input("수정 할 항목 입력>> "))

	for item in tList :
		if seq == item['seq'] :
			select_todo = item
			print("찾았습니다!")
			print_row(select_todo)
			break

	if select_todo != None :
		while True :
			menu_list = ["MOIFY MENU", "상태수정", "할일수정", "삭제", "확인"]
			no = _factory[0](menu_list)
			print("----->", no)
			if no == len(menu_list) - 1:
				print("--- 실행 취소 - main으로 이동 합니다 ---")
				return

			if no == 3:
				tList.remove(select_todo)
				print("--- 삭제 성공 - main으로 이동 합니다 ---")
				return
			
			modify_fn_factory[no]()
	else :
		print("선택 항목은 목록에 없습니다!")

def ex_todo() :
	sys.exit()

# List 구조에 함수를 저장
_factory = [menu, insert_todo, modify_todo]

def main() :
	while True :
		print_list()
		menu_list = ["MENU", "추가", "수정", "종료"]
		no = _factory[0](menu_list)
		print(f"{no}번 선택하셨습니다.")
		if no == len(menu_list)-1 :
			print("{:-^20}".format("프로그램 종료"))
			break
		print("="*40)
		_factory[no]()
		print("="*40)

if __name__ == '__main__':
	res = main()