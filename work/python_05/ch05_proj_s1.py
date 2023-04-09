import sys

tList = [
	{"seq":1, "title":"친구 만나기", "done":True},
	{"seq":2, "title":"과제 하기", "done":False},
	{"seq":3, "title":"청소 하기", "done":False},
	{"seq":4, "title":"붕어 밥 주기", "done":True},
]
sequence = 5

def menu(*todoItem):
	print("\n{:*^51}".format(todoItem[0]))
	for i, item in enumerate(todoItem) :
		if i!= 0 :
			print(i,".",item, sep="", end="     ")
	check = int(input("\n선택>> "))
	
	while not(check in range(1, len(todoItem))) :
		print(">>해당 번호가 존재하지 않습니다.")
		check = int(input("\n선택>> "))

	return check


def list_todo() :
	global sequence
	
	while True :
		form_todo()
		check = menu("할일관리","추가하기","수정하기","종료")
		print(f">>{check}번 입력하셨습니다.")
		if check == 1:
			print("\n{:*^53}".format("추가"))
			add_todo()
			sequence = sequence + 1

		elif check == 2 :
			print("\n{:*^53}".format("수정"))
			edit_todo()
			
		elif check == 3 :
			print("\n{:*^53}".format("종료"))
			exit_todo()


# 폼양식
def form_todo():
	print("\n"+"-"*55+"\n{}".format("김코딩의 할일 리스트"))
	print("-"*55)
	
	for i, p in enumerate(tList) :
		if p['done'] == True :
			p['done']  = str("완  료")
		elif p['done'] == False :
			p['done']  = str("미완료")
		print("[{: ^1}]{: <3}| {: <40}" .format(p['seq'], p['done'], p['title']))
	print("-"*55)
	print(p['seq'], "건이 있습니다.")
	return True


# 추가하기
def add_todo():
	num = {
		"seq": sequence,
		"title": input("새로운 할일을 입력해주세요\n>>"),
		"done": bool(False)
	}
	tList.append(num)


# 수정하기
def edit_todo():
	global sequence
	
	if form_todo():
		mod_seq = int(input("해당 번호 입력해주세요>> "))
		while True :
			for p in tList :
				if p["seq"] == mod_seq :
					no = menu("수정선택","상태수정","할일수정","삭제")
					if no == 1 :
						tf_no = menu("완료여부","완료","미완료")
						if tf_no == 1:
							p["done"] = True
						elif tf_no == 2:
							p["done"] = False
						print(">>상태 변경 완료했습니다.")

					elif no == 2 :
						p["title"] = input("(할일)수정할 내용을 입력해주세요>> ")
						print(">>입력하신 내용 수정 완료했습니다.")

					elif no == 3 :
						del tList[mod_seq-1]
						print(">>삭제 완료했습니다.")
					return
				
			print(">>앗! 해당 번호는 없습니다.")
			mod_seq = int(input("다시 입력해주세요>> "))
		
# 종료
def exit_todo():
	sys.exit(0)

if __name__ == "__main__":
	list_todo()