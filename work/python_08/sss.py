import random

class GameObject:
    def __init__(self, start_x, start_y, distance):
        self.x = start_x
        self.y = start_y
        self.distance = distance

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def collide(self, obj):
        if self.x == obj.get_x() and self.y == obj.get_y():
            return True
        else:
            return False


class Bear(GameObject):
    def move(self):
        key = input("왼쪽(a), 위(w), 아래(s), 오른쪽(d) >> ")
        print()
        if key.lower() == "a" and self.y > 0:
            self.y -= self.distance
        elif key.lower() == "w" and self.x > 0:
            self.x -= self.distance
        elif key.lower() == "s" and self.x < 9:
            self.x += self.distance
        elif key.lower() == "d" and self.y < 19:
            self.y += self.distance

    def get_shape(self):
        return 'B'


class Fish(GameObject):
    def move(self):
        key = random.randint(0, 3)
        if key == 0 and self.y > 0:
            self.y -= self.distance
        elif key == 1 and self.x > 0:
            self.x -= self.distance
        elif key == 2 and self.x < 9:
            self.x += self.distance
        elif key == 3 and self.y < 19:
            self.y += self.distance

    def get_shape(self):
        return '@'


class Game:
    def __init__(self):
        self.map = [['-' for _ in range(20)] for _ in range(10)]
        self.bear = Bear(0, 0, 1)
        self.fish = Fish(random.randint(0, 9), random.randint(0, 19), 1)
        self.run()

    def run(self):
        print("** Bear의 Fish 먹기 게임을 시작합니다 **")
        print()
        self.draw_map()
        move_fish_array = self.move_fish()
        index = 0

        while True:
            self.bear.move()
            if move_fish_array[index] == 1:
                self.fish.move()

            index += 1
            if index == 5:
                move_fish_array = self.move_fish()
                index = 0

            self.draw_map()
            if self.bear.collide(self.fish):
                print("Woooow- Good!!")
                break

    def draw_map(self):
        for i in range(10):
            for k in range(20):
                self.map[i][k] = '-'
        self.map[self.fish.get_x()][self.fish.get_y()] = self.fish.get_shape()
        self.map[self.bear.get_x()][self.bear.get_y()] = self.bear.get_shape()

        for row in self.map:
            print(' '.join(row))
        print()

    def move_fish(self):
        return [random.randint(0, 1) for _ in range(5)]

game_with_bear = Game()
