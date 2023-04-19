# from music import Music
class Music :
    def __init__(self, track, title, singer):
        self.track = track
        self.title = title
        self.singer = singer

    def play(self):
        print(f"{self.track}번 트랙 {self.singer}의 {self.title} 실행중입니다.")

    def list(self): # 실시간 리스트 확인위해 추가
        return f"[{self.track}] {self.singer} | {self.title}"

class MusicPlayer :
	def __init__(self) :
		self.factory = [self.menu, self.insert, self.remove, self.playAll, self.finish]
		self.musicList = []
		self.sequence = 1
		while True :
			print("{::^40}".format("Music Player"))
			no = self.menu("add", "remove", 'musicAll', 'exit')

			self.factory[no]()

	def menu(self, *items) :
		for i, item in enumerate(items):
			print(f"({i+1}){item}", end="   ")
		no = int(input(">> "))
		while not()

		while not(no in range(1, len(items)+1) ) :
			print("입력 범위를 초과 했습니다!")
			no = int(input("다시 입력>>"))
		while not no in range(1, len(items)+1) :
			try :
				no = int(input("메뉴 번호를 입력해주세요>> "))
			except :
				print("입력 범위를 초과했습니다!")

		return no

	def insert(self) :
		print("새 곡 추가")
		while True :
			title = input("{:-^30}".format("새 곡 입력>> "))
			if title == "그만" : break
			singer = input("{:-^30}".format("가수 입력>> "))
			self.musicList.append(Music(self.sequence, title, singer))
			self.sequence += 1

	def remove(self) :
		pass

	def playAll(self) :
		pass

	def finish(self) :
		pass

if __name__ == '__main__':
	MusicPlayer()