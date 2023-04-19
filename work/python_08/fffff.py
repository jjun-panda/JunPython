import sys
from gettext import find

from music import Music


class MusicPlayer :
	def __init__(self):
		self.factory = [self.menu, self.insert, self.remove, self.playAll, self.finish]
		self.musicList = []
		self.sequence = 1

		while True :
			print("{::^40}".format("Music Player"))
			no = self.menu("추가","제거","전곡실행","종료")

			self.factory[no]()


	def menu(self, *items):
		for i, item in enumerate(items):
			print(f"({i+1}){item}", end=" ")
		no = int(input(">>"))
		# 유효성 검사
		while not(no in range(1, len(items)+1) ) :
			print("입력 범위를 초과 했습니다!")
			no = int(input("다시 입력>>"))

		return no


	def insert(self):
		print("----- 새 곡 추가 -----")
		while True :
			title = input("곡목 입력>>")
			if title == "그만" : break
			singer = input("가수 입력>>")
			self.musicList.append(Music(self.sequence, title, singer))
			self.sequence += 1


	def remove(self):
		print("----- 곡 제거 -----")
		seq = int(input("삭제 할 번호 입력>>"))
		findMusic = None
		for music in self.musicList :
			if seq == music.getTrack() :
				findMusic = music
				break

		if findMusic != None :
			print(findMusic, "삭제")
			self.musicList.remove(findMusic)


	def playAll(self):
		print("----- 전 곡 재생 -----")
		for music in self.musicList :
			music.play()


	def finish(self):
		print("--- 뮤직 플에이어 종료! ---")
		sys.exit(0)


if __name__ == '__main__':
	MusicPlayer()