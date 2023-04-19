class Player:
	def __init__(self, name):
		self.username = name
		self.word_play = None
		self.word_length = None

	# 참가자 단어 입력
	def play_word(self):
		self.word_play = input(f"[{self.username}] >> ")
		return self.word_play
	
	# 끝말잇기 일치여부
	def succeed(self, last_word):
		return last_word == self.word_play[0]

class WordGameApp:
	def __init__(self):
		self.players = None
		self.word = None
		self.word_length = 0
		self.start()

	# 게임 시작
	def start(self):
		print("{:-^40}".format(" 끝말잇기 게임에 오신 것을 환영합니다. "))
		self.players = self.get_players()
		self.play()

	# 참가자 인원
	def get_players(self):
		players = []    # 입력된 게임 참가자 이름의 리스트
		# number = int(input("게임에 참가하는 인원은 몇 명인가요(2명 이상)>> "))
		# while number < 2 :
		# 	number = int(input("2명 이상 참가해야됩니다! 다시 입력해주세요>> "))
		# for i in range(number): #사용자가 입력한 숫자만큼 참가자이름 입력 요청한다.
		# 	name = input(f"{i+1}번 참가자의 이름을 입력해주세요>> ")
		# 	players.append(Player(name))
		while True :
			try:	
				number = int(input("게임에 참가하는 인원은 몇 명인가요(조건: 2명 이상)>> "))
				if number == 0 :
					print("게임 하기 싫은가요...? 2명 이상 참가해야됩니다!")
				elif number < 2 : # elis number == 1로 써도 동일
					print("혼자 하고 싶은가요? 미안하지만 2명 이상 참가해야됩니다!")
				else :
					break
			except:
				print("숫자만 입력해주세요!")
		for i in range(number): #사용자가 입력한 숫자만큼 참가자이름 입력 요청한다.
			name = input(f"{i+1}번 참가자의 이름을 입력해주세요>> ")
			players.append(Player(name))
		return players
	
	# 게임 옵션 및 진행
	def play(self):
		# 글자 길이 설정
		print("\n" + "=" * 48 + "\n")
		while True :
			try:
				self.word_length = int(input("몇 글자 단어로 진행할 것인가요>> "))
				if self.word_length == 0:
					print("0글자요...? 게임하기 싫은건가요?\n2글자부터 시작해야됩니다!")
				elif self.word_length == 1:
					print("1글자요...? 1글자로는 무슨 게임입니까?\n2글자부터 시작해야됩니다.")
				else:
					break
			except:
				print("숫자만 입력해주세요!")

		# 시작할 단어 설정
		get_word = input("시작할 단어를 입력해주세요>> ")
		while not len(get_word) == self.word_length:
			get_word = input(f"앗! {len(get_word)}글자 입력하셨네요! 입력된 단어는 {self.word_length}글자가 아닙니다. \n{self.word_length}글자 단어로 다시 입력해주세요>> ")
		self.word = get_word

		# 게임 시작
		print("\n" + "=" * 48 + "\n")
		print(f"환영합니다! 끝말잇기 게임을 시작하겠습니다.\n참가자는 {', '.join([player.username for player in self.players])}님 이며, 모두 {len(self.players)}명 입니다.")
		print(f"시작할 단어는 '{get_word}'이며, {self.word_length}글자 입니다.")
		print(f"\n첫 글자 '{self.word[-1]}'에 들어갈 단어를 입력해주세요!\n")

		user = 0 # 참가자 차례 순서대로 진행
		while True:
			print(user)
			print(len(self.players))
			player = user % len(self.players)
			print(player)
			last_word = self.word[-1]
			game_user = self.players[player]
			game_user.play_word()
			
			if not game_user.succeed(last_word):
				print(f"\n[{game_user.username}님 패배!]")
				print(f"당신은 방금 입력하신 첫 글자는 '{game_user.word_play[0]}'이며, '{last_word}'와/과 불일치합니다!")
				print("모두한테 족발 하나씩 사주세요^^")
				break
			elif len(game_user.word_play) != self.word_length:
				print(f"\n[{game_user.username}님 패배!]")
				print(f"당신은 {len(game_user.word_play)}글자를 입력하셨습니다!(조건: {self.word_length}글자)")
				print("모두한테 족발 하나씩 사주세요^^")
				break
					
			self.word = game_user.word_play
			user += 1

		self.play_again()

	# 재게임 여부
	def play_again(self):
		print("\n" + "=" * 48 + "\n")
		# while True :
		# 	try:
		# 		again = input("게임을 다시 하겠습니까? (y/n)>> ")
		# 		if again.lower() == "y": # 대문자, 소문자 구분 없이 입력가능하도록 개선
		# 			self.__init__()
		# 		elif again.lower() == "n":
		# 			print("게임을 종료합니다.")
		# 			break
		# 		else:
		# 			print("y 또는 n 만 입력해주세요!")
		# 	except:
		# 		print("예상치 못한 오류가 발생했습니다. 다시 입력해주세요!")
		again = input("다시 게임을 하시겠습니까? (y/n)>> ")
		while not (again in["y","n"]) :
			print("y 또는 n 만 입력해주세요!")
			again = input("다시 게임을 하시겠습니까? (y/n)>> ")
		if again.lower() == "y": # 대문자, 소문자 구분 없이 입력가능하도록 개선
			self.__init__()
		elif again.lower() == "n":
			print("게임을 종료합니다.")

lets_play = WordGameApp()
