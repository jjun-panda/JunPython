# 실습 : 성적 출력 프로그램
import sys
# import pandas as pd

sList = []

sequence = 1

def menu(*menuItem) :
	print("\n{:-^48}".format(menuItem[0]))
	for i, item in enumerate(menuItem) :
		if i!= 0 :
			print(i,".",item, sep="", end="\t")
	num = int(input("\n선택>> "))

	while not(num in range(1, len(menuItem))) :
		print(">>잘못된 입력하셨습니다.")
		num = int(input("\n선택>> "))
		
	print("-"*50)
	return num

def list_std() :
	global sequence
	
	while True:
		num = menu("성적관리 시스템","등록","결과","검색","수정","삭제","종료")
		print(f">> {num}번 선택했습니다.")
		if num == 1:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("입력")+"\n"+"*"*50)
			intput_std()
			sequence = sequence + 1
		elif num == 2:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("출력")+"\n"+"*"*50)
			output_std()
		elif num == 3:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("검색")+"\n"+"*"*50)
			search_std()
		elif num == 4:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("수정")+"\n"+"*"*50)
			modify_std()
		elif num == 5:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("삭제")+"\n"+"*"*50)
			delete_std()
		elif num == 6:
			print("\n"+"*"*50+"\n"+"{: ^48}".format("종료")+"\n"+"*"*50)
			end_std()
			break
		else:
			print(">>잘못된 입력하셨습니다.")

# 입력
def intput_std() :
	global sequence
	std = {
		"seq" : sequence,
		"name" : input("이름>> "),
		"kor" : int(input("국어점수>> ")),
		"eng" : int(input("영어점수>> ")),
		"mat" : int(input("수학점수>> ")),
		"total" : 0,
		"avg" : 0.0,
		"grade" : "F",
		"rank" : 1
	}
	std["total"] = std["kor"] + std["eng"] + std["mat"]
	std["avg"] = round(std["total"] / 3.0, 2)
	std["grade"] = "A" if std["avg"] >= 90 else "B" if std["avg"] >= 80 else "C" if std["avg"] >= 70 else "D" if std["avg"] >= 60 else "F"
	
	# std["rank"] = std["avg"].rank(ascending=False)
	# sList = pd.DataFrame(sList)
	sList.append(std)


# 출력
def output_std() :
	print("{: >3}|{: ^20}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format("seq", "name", "kor", "eng", "mat", "total", "avg", "grade", "rank"))
	print("-"*88)
	for i, p in enumerate(sList) :
			print("{: >3}|{: ^20}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(p['seq'], p['name'], p['kor'], p['eng'], p['mat'], p['total'], p['avg'], p['grade'], p['rank']))
	return True
	

# 검색
def search_std() :
	search = input("무엇을 검색하시겠습니까? [예시: 90, kim]\n검색어>> ")
	while len(search) == 0 :
		print(">>아무것도 입력하지 않으셨습니다!")
		search = input("다시 입력해주세요. 검색어>> ")
	try:
		search = int(search)
	except ValueError:
		pass

	newList = [];
	for p in sList :
		if p['name'] == search :
			newList.append(p)
		elif p['kor'] == search :
			newList.append(p)
		elif p['eng'] == search :
			newList.append(p)
		elif p['mat'] == search :
			newList.append(p)
	
	if len(newList) == 0 :
		print(">>검색결과가 없습니다.")
		return False
	else :        
		print("{: >3}|{: ^20}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format("seq", "name", "kor", "eng", "mat", "total", "avg", "grade", "rank"))
		print("-"*88)
		for i, p in enumerate(newList) :
				print("{: >3}|{: ^20}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}|{: ^8}".format(p['seq'], p['name'], p['kor'], p['eng'], p['mat'], p['total'], p['avg'], p['grade'], p['rank']))
	return True

# 수정
def modify_std() :
	if output_std() :
		mod_seq = int(input("수정할 번호 입력해주세요>> "))
		for p in sList :
			if p["seq"] == mod_seq :
				no = menu("수정선택","이름수정","점수수정")
				if no == 1 :
					p["name"] = input("새 이름 입력>> ")
				elif no == 2 :
					stu_no = menu("과목","국어","영어","수학")
					if stu_no == 1 :
						p["kor"] = int(input("국어점수 입력>> "))
					elif stu_no == 2 :
						p["eng"] = int(input("영어점수 입력>> "))
					elif stu_no == 3 :
						p["mat"] = int(input("수학점수 입력>> "))
					else :
						print(">>잘못된 번호입니다.")
				else :
					print(">>잘못된 번호입니다.")
				print(">>수정 완료했습니다.")

# 삭제
def delete_std() :
	if output_std() :
		del_seq = int(input("삭제할 번호 입력해주세요>> "))
		del sList[del_seq-1]
		print(">>삭제 완료했습니다.")
		# for p in sList :
		# if p["seq"] == del_seq :
		#     del sList[del_seq-1]
		#     print("삭제 완료했습니다.")
		# else :
		#     print("존재하지 않는 번호입니다.")
		
# 종료
def end_std() :
	sys.exit()
	pass

if __name__ == "__main__":
	list_std()