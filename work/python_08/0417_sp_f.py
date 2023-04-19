import random
import sys

class GameObject :
	def __init__(self, startX, startY) :
		self.x = startX
		self.y = startY

	def move(self, target):
		if target.lower() == "a" or target.lower() == "d" : # 좌우
			if target.lower() == "a" :
				self.x -= 1 # left
			else :
				self.x += 1 # right
		elif target.lower() == "s" or target.lower() == "w" : # 상하
			if target.lower() == "s" :
				self.y += 1 # down
			else :
				self.y -= 1 # up
		# abs() = 절대값 구하는 내장 함수. 입력값이 음수라면 양수로 변환하고, 양수라면 그대로 반환
		self.x = abs(self.x % 20)
		self.y = abs(self.y % 10)
	
	def getX(self) :
		return self.x

	def getY(self) :
		return self.y
	
	def getShape(self) :
		return self.shape
	
	def collide(self, p) :
		if self.x == p.getX() and self.y == p.getY() :
			return True
		else :
			return False 
	
class Bear(GameObject) :
	def __init__(self, x, y) :
		self.shape = "B"
		super().__init__(x, y)
	
class Fish(GameObject) :
	def __init__(self, x, y) :
		self.shape = "@"
		super().__init__(x, y)

class Game :
	def __init__(self) :
		# self.map = [["-" for i in range(20)] for i in range(10)]
		self.bear = Bear(0, 0)
		self.fish = Fish(random.randint(0, 9), random.randint(0, 19))
		self.run()

	def menu(self) :
		no = input("left(a), right(d), down(s), up(w) >> ")
		
		while no.lower() not in ['a', 's', 'd', 'w']:
			print("\nWarning: Please enter only a, s, d, w\n")
			no = input("left(a), right(d), down(s), up(w) >> ")
		
		return no
	
	# 게임 시작
	def run(self) :
		print("**** Bear가 Fish를 잡아먹다! ****")
		self.count = 0

		while True :
			self.draw()
			target = self.menu()
			self.action(self.bear, target)
			self.count += 1
			if self.count % 1 == 0 :
				for i in range(random.randint(1, 1)) :
					self.action(self.fish, random.choice(['a', 's', 'd', 'w']))

	# 맵 그리기
	def draw(self) :
		self.map = [["-" for i in range(20)] for i in range(10)]
		self.map[self.bear.getY()][self.bear.getX()] = self.bear.getShape()
		self.map[self.fish.getY()][self.fish.getX()] = self.fish.getShape()

		for row in self.map:
			for col in row:
				print(col, end="")
			print()

	def action(self, animal, target):
		animal.move(target)
		targetX = animal.getX()
		targetY = animal.getY()
		self.map[targetY][targetX] = animal.getShape()

		if self.bear.collide(self.fish):
			print("Game Over")
			sys.exit(0)
		# self.map[animal._y][animal._x] = "-"

game = Game()