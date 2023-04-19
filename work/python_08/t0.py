# 끝말 잇기 게임

class Player :
	def __init__(self, user):
		self.user = user
		self.word = ""

	def getWordFromUser(self):
		self.word = input(f"{self.user}>>")
		return self.word

	def checkSuccess(self, word):
		return True if word[-1] == self.word[0] else False

	def __str__(self):
		return self.user



class WordGameApp :
	def __init__(self):
		print("끝말잇기 게임을 시작합니다...")
		self.n = int(input("게임에 참가하는 인원은 몇명입니까>>"))
		self.userList = []
		for i in range(self.n) :
			self.userList.append(Player(input("참가자 이름을 입력하세요>>")))

		self.run()


	def run(self):
		self.check = True
		self.cnt = 0
		self.player = None
		self.word = "아버지"
		self.tmpWord = None
		while self.check:
			self.player = self.userList[self.cnt % len(Player(user))]
			self.tmpWord = self.player.getWordFromUser()
			self.check = self.player.checkSuccess(self.word)
			self.word = self.tmpWord
			self.cnt += 1

		print(f"{self.player}가 졌습니다.")


if __name__ == '__main__':
		WordGameApp()