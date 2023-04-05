pList = [
]

while True:
	print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
	no = int(input("선택: "))
	if no == 1 :
		print("{:-^50}".format(" 입력기능 "))
		people = {}
		people["name"] = input("성명>>> ")
		people["phone"] = input("전화>>> ")
		people["addr"] = input("주소>>> ")
		pList.append(people)
		print("모두 입력 완료!")
	elif no == 2 :
		print("{:-^50}".format(" 출력기능 "))
		print("{:^3}{:^10}{:^15}{:^20}".format("번호", "성명", "전화", "주소") )
		print("-"*50)
		for i, p in enumerate(pList) :
			print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))

	elif no == 3 :
		print("{:-^50}".format(" 검색기능 "))

		search = input("어떤 것을 검색하시겠습니까?>>> ")
		while(len(search) == 0) :
			print("입력하지 않았네요!")
			search = input("다시 입력해주세요>>> ")
		sList = [];

		for i, p in enumerate(pList) :
			if(p["name"] == search) :
				sList.append(p);
			elif(p["phone"] == search) :
				sList.append(p);
			elif(p["addr"] == search) :
				sList.append(p);
		if(len(sList) == 0) :
			print(f"'{search}'검색한 결과, 리스트에 없습니다.")
		else :       
			print(f"'{search}'검색한 결과 입니다.\n")

			for i, p in enumerate(sList) :
				print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))

	elif no == 4 :
		print("{:-^50}".format(" 수정기능 "))
		print("{:^3}{:^10}{:^15}{:^20}".format("번호", "성명", "전화", "주소") )
		print("-"*50)
		for i, p in enumerate(pList) :
			print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
		print("\n")
		edit = int(input("어떤 부분을 수정하겠습니까?(해당 번호만 입력)>>> "))
		while(len(pList) < edit or edit <= 0) :
			print("해당 번호 내 리스트가 없습니다!")
			edit = int(input("다시 입력해주세요>>> "))
		
		edit -= 1;

		print("\n수정 할 항목을 입력 하세요.")
		print("1.성명 2.전화번호 3.주소 4.모두")
		modify_select = int(input("선택>>> "))
		if(modify_select == 1) :
			pList[edit]["name"] = input("새 이름 입력>>> ")
		elif (modify_select == 2):
			pList[edit]["phone"] = input("새 전화번호 입력>>> ")
		elif (modify_select == 3):
			pList[edit]["addr"] = input("새 주소 입력>>> ")
		elif (modify_select == 4) :
			pList[edit]["name"] = input("새 이름 입력>>> ")
			pList[edit]["phone"] = input("새 전화번호 입력>>> ")
			pList[edit]["addr"] = input("새 주소 입력>>> ")
		else :
			print("선택 항목이 없습니다!")

	elif no == 5 :
		print("{:-^50}".format(" 삭제기능 "))
		print("{:^3}{:^10}{:^15}{:^20}".format("번호", "성명", "전화", "주소") )
		print("-"*50)
		for i, p in enumerate(pList) :
			print("{:^3}{:^10}{:^15}{:^20}".format(i+1,p["name"],p["phone"],p["addr"]))
		print("\n")
		dele = int(input("어떤 부분을 삭제하겠습니까?(해당 번호만 입력)>>>"))
		while(len(pList) < dele or dele <= 0) :
			print("해당 번호 내 리스트가 없습니다!")
			dele = int(input("다시 입력해주세요>>> "))

		del pList[dele-1]
		print(f"삭제 완료!")

	elif no == 6 :
		print("{:-^50}".format(" 종료-굿바이 "))
		break

	else :
		print("{:-^50}".format(" 선택 사항 없슴 "))

	print()

print("다음 기회에 만나요~")