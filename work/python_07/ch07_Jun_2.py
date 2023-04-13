class Saram :
	def __init__(self, seq, name, phone, addr) :
		self.seq = seq
		self.name = name
		self.phone = phone
		self.addr = addr
		
	def	__str__(self) :
		# print("calling")
		return "[{: <3}] {: <5} {: <14} {: <8}".format(self.seq, self.name, self.phone, self.addr)
	
	def setSeq(self, seq):
		self.seq = seq
		
	def setName(self, name):
		self.name = name
		
	def setPhone(self, phone):
		self.phone = phone

	def setAddr(self, addr):
		self.addr = addr
		
	def getSeq(self):
		return self.seq
	
	def getName(self):
		return self.name
	
	def getPhone(self):
		return self.phone

	def getAddr(self):
		return self.addr

# 메뉴선택
class Menu :
	def draw(self) :
		print("\n{:*^34}".format(" MENU "))
		print("1.input 2.output 3.search 4. modify 5.dele 6.end")
		return int(input("Choose>> "))

# 주소록 리스트
class List :
	def __init__(self, sList) :
		self.sList = sList

	def draw(self):
		print()
		print("{:-^34}".format(" User List "))
		for user in self.sList :
			print(user)

# 사람 추가
class InputSaram :
	def __init__(self, sList, sequence):
		self.sList = sList
		self.sequence = sequence

	def draw(self):
		print()
		print("{:-^34}".format(" User Infor "))
		seq = self.sequence
		name = input("Input name>> ")
		phone = input("Input phone>> ")
		addr = input("Input addr>> ")
		self.addSaram(seq, name, phone, addr)
		self.sequence += 1
		print("\n>>Registration successful!\n  [{: <3}] {: <5} {: <14} {: <8}".format(seq, name, phone, addr))

	def addSaram(self, seq, name, phone, addr):
		saram = Saram(seq, name, phone, addr)
		self.sList.append(saram)

# 사용자 검색
class SearchSaram :
	def __init__(self, sList, sequence) :
		self.sList = sList
		self.sequence = sequence

	def draw(self):
		print()
		print("{:-^34}".format(" User Search "))
		seq = int(input("Input search>> "))

# 사용자 수정
class ModifySaram :
	def __init__(self, sList, sequence) :
		self.sList = sList
		self.sequence = sequence

	def draw(self):
		print()
		print("{:-^34}".format(" User Modify "))
		
		pass

# 사용자 삭제
class DeleteSaram :
	def __init__(self, sList):
		self.sList = sList
	
	def draw(self):
		print()
		print("{:-^34}".format(" User Delete "))
		seq = int(input("Input seq>> "))
		found = False

		for i, user in enumerate(self.sList):
			if user.getSeq() == seq:
				del self.sList[i]
				found = True
				break

		if found:
			print("\n>>Deletion successful!")
		else:
			print("\n>>No user with the sequence number found.")

# 주소록
class PhoneBook :
	def __init__(self) :
		self.sList = [
			Saram(101, "Hong", "010-1234-1234", "Seoul"),
			Saram(102, "Kim", "010-1234-1234", "Busan"),
			Saram(103, "Park", "010-1234-1234", "Ansan")
		]
		sequence = 104

		self.factory = [Menu(), InputSaram(self.sList, sequence), List(self.sList), SearchSaram(self.sList, sequence), ModifySaram(self.sList, sequence), DeleteSaram(self.sList)]
		
		print("{:-^29}".format(" 주소록 관리 "))
		self.play()
	
	def play(self) :
		no = self.factory[0].draw()
		if no == 6 :
			print("\nGoodbye!")
			return
		
		self.factory[no].draw()
		self.play()

if __name__ == "__main__":
	PhoneBook()