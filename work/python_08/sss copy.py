import random
import sys


class GameObject:
	def __init__(self, startX, startY):
		self.x = startX
		self.y = startY

	def move(self, target):
		self._x = self.x
		self._y = self.y

		if target.lower() == "a" or target.lower() == "f":
			if target.lower() == "a":
				self.x -= 1
			else:
				self.x += 1
		else:
			if target.lower() == "s":
				self.y += 1
			else:
				self.y -= 1

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
		else:
			return False


class Bear(GameObject):
	def __init__(self, startX, startY):
		self.shape = "B"
		super().__init__(startX, startY)


class Fish(GameObject):
	def __init__(self, startX, startY):
		self.shape = "@"
		super().__init__(startX, startY)


class Game:
	def __init__(self):
		self.bear = Bear(0, 0)
		self.fish = Fish(random.randint(0, 9), random.randint(0, 19))
		self.run()

	def menu(self):
		no = input("left(a), right(d), down(s), up(w) >> ")

		while no not in ['a', 's', 'd', 'w']:
			print("Warning: Please enter only a, s, d, w")
			no = input("left(a), right(d), down(s), up(w) >> ")

		return no

	def run(self):
		print("**** Bear가 Fish를 잡아먹다! ****")
		self.draw()
		self.count = 0

		while True:
			target = self.menu()
			self.action(self.bear, target)

			self.count += 1
			if self.count % 4 == 0 or self.count % 5 == 0:
				for i in range(random.randint(1, 1)):
					self.action(self.fish, random.choice(['a', 's', 'd', 'w']))

			self.draw()

	def draw(self):
		self.map = [["-" for i in range(20)] for i in range(10)]
		self.map[self.bear.getY()][self.bear.getX()] = self.bear.getShape()
		self.map[self.fish.getY()][self.fish.getX()] = self.fish.getShape()

		for row in self.map:
			for col in row:
				print(col, end="")
			print()

	def action(self, animal, target):
		animal.move(target)
		if self.bear.collide(self.fish):
			print("게임 종료!")
			sys.exit(0)

		targetX = animal.getX()
		targetY = animal.getY()
		self.map[targetY][targetX] = animal.getShape()
		self.map[animal._y][animal._x] = "-"


if __name__ == '__main__':
	game = Game()
