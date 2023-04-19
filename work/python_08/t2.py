# Bear Fish Game ver.2
import random
import sys, math


class Animal :
	def __init__(self, y, x):
		self.x = x
		self.y = y

	def move(self, target):
		self._x = self.x
		self._y = self.y
		if target == "a" or target == "f" :
			if target == "a" :
				self.x -= 1
			else :
				self.x += 1
		else :
			if target == "d" :
				self.y -= 1
			else :
				self.y += 1

		self.x = abs(self.x % 20)
		self.y = abs(self.y % 10)


	def getX(self): return self.x
	def getY(self): return self.y
	def getShape(self): return self.shape

	def collide(self, p):
		return True if self.x == p.getX() and self.y == p.getY() else False



class Bear(Animal) :
	def __init__(self, x, y):
		self.shape = "B"
		super().__init__(x, y)


class Fish(Animal) :
	def __init__(self, x, y):
		self.shape = "@"
		super().__init__(x, y)


class Game :
	table = []

	def __init__(self):
		print("** Bear의 Fish 먹기 게임을 시작 합니다. **")
		for i in range(10) :
			self.table.append(list("-"*20))

		#배열 생성 후에 움직여야 한다.
		self.bear = Bear(5,5)
		self.fish = Fish(6,8)
		self.action(self.bear, "s")
		self.action(self.fish, "s")
		self.run()


	def menu(self):
		no = input("외쪽(a), 아래(s), 위(d), 오른쪽(f) >>")
		while not(no=="a" or no=="s" or no=="d" or no=="f") :
			print("경고: a s d f중에 다시 입력!")
			no = input("외쪽(a), 아래(s), 위(d), 오른쪽(f) >>")

		return no


	def draw(self):
		# 화면 그리기
		for row in self.table:
			for col in row:
				print(col, end="")
			print()


	def action(self, animal, target):
		if self.bear.collide(self.fish) :
			print("게임 종료!")
			sys.exit(0)

		animal.move(target) # 위지 이동
		targetX = animal.getX() # 변경 위치로 shape 이동
		targetY = animal.getY()
		self.table[targetY][targetX] = animal.getShape()
		self.table[animal._y][animal._x] = "-"


	def run(self) :
		self.draw()
		self.cnt = 0;
		while True :
			target = self.menu()
			self.action(self.bear, target)
			# Bear가 5번 움직일 동안 random하게 Fish가 두번 움직인다.
			self.cnt += 1
			if self.cnt % 4 == 0 or self.cnt % 5 == 0 :
				for i in range(random.randint(2, 5)) :
					self.action(self.fish, random.choice(['a', 's', 'd', 'f']))

			self.draw()


if __name__ == '__main__':
	Game() # Game 클래스 생성자