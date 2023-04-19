import random
import sys, math

class Animal :
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.shape = "B"

	def move(self, target):
		self._x = self.x
		self._y = self.y
		if target == "a" or target == "d" :
			if target == "a" :
				self.x -= 1
			else :
				self.x += 1
		else :
			if target == "w" :
				self.y -= 1
			else :
				self.y += 1

		self.x = abs(self.x % 20)
		self.y = abs(self.y % 10)

	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getShape(self):
		return self.shape
	
	def collide(self, p):
		if self.x == p.getX() and self.y == p.getY():
			return True
		else :
			return False
		
class Bear(Animal) :
	def __init__(self, x, y):
		super().__init__(x, y)
		self.shape = "B"

class Fish(Animal) :
	def __init__(self, x, y):
		super().__init__(x, y)
		self.shape = "@"

class Game :
	table = []
	
	def __init__(self):
		print("** Bear의 Fish 먹기 게임을 시작합니다 **")
		for i in range(10):
			self.table.append(list("-"*20))
		
		self.bear = Bear(5,5)
		self.fish = Fish(6,8)
		self.action(self.bear, "s")
		self.action(self.fish, "s")
		self.run()
		
	def menu(self):
		no = input("외쪽(a), 아래(s), 위(w), 오른쪽(d) >> ")
		while not(no=="a" or no=="s" or no=="w" or no=="d") :
			print("경고: a s w d중에 다시 입력!")
			no = input("외쪽(a), 아래(s), 위(w), 오른쪽(d) >> ")
		return no
	
	def draw(self):
		# 화면 그리기
		for row in self.table:
			for col in row:
				print(col, end="")
			print()
		
	def action(self, animal, target):
		if self.bear.collide(self.fish) :
			print("게임 종료")
			sys.exit(0)

		animal.move(target) # 위치 이동
		targetX = animal.getX() # 변경 위치로 shape 이동
		targetY = animal.getY()
		self.table[targetY][targetX] = animal.getShape()
		self.table[animal._y][animal._x] = "-"

	def run(self) :
		self.draw()
		self.count = 0
		while True :
			target = self.menu()
			self.action(self.bear, target)
			#action(fish, rendTarget)
			self.count += 1
			if self.count % 4 == 0 or self.count % 5 == 0:
				for i in range(random.randint(2,5)) :
					self.action(self.fish, random.choice(['a','s','d','w']))
			self.draw()
		
if __name__ == "__main__":
	Game()