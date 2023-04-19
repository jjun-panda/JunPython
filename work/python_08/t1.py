class GameObject :
    def __init__(self, startY, startX, distance):
        # 이동 후 이전 위치 저장
        self._x = 0
        self._y = 0 
        self.x = startX
        self.y = startY
        self.distance = distance # 한번 이동 거리 a좌 s하 d상 f우
        self.move(distance)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def collide(self, p):
        return True if self.x == p.getX() and self.y == p.getY() else False

    def move(self, distance):
        # 이동 후 이전 위치를 "-"로 변경 하기 위한 속성
        self._x = self.x
        self._y = self.y
        if distance == "a" or distance == "f" :
            # 좌우 이동
            if distance == "a" :
                self.x -= 1
            else :
                self.x += 1
        else :
            # 상하 이동
            if distance == "d" :
                self.y -= 1
            else :
                self.y += 1


    def getShape(self):
        return self.shape


class Bear(GameObject) :
    shape = "B"
    def __init__(self, startX, startY, distance):
        super().__init__(startX, startY, distance)



class Fish(GameObject) :
    shape = "@"
    def __init__(self, startX, startY, distance):
        super().__init__(startX, startY, distance)

class Game :
    # 10행 20열 출력
    lis = []
    def __init__(self) :
        for i in range(10) :
            s_lis = []
            for j in range(20) :
                s_lis.append("-")
            self.lis.append(s_lis)

        # Bear와 Fish를 생성 테스트 해보기
        self.bear = Bear(4, 5, "s")
        self.fish = Fish(8, 15, "s")

        self.draw()
        while True :
            target = input("방향 입력(a(좌)/s(하)/d(상)/f(우))>>")
            self.bear.move(target)

            self.draw()


    def draw(self) :
        # bear의 위치
        self.lis[self.bear.getY()][self.bear.getX()] = "B"
        self.lis[self.bear._y][self.bear._x] = "-"
        # fish의 위치
        self.lis[self.fish.getY()][self.fish.getX()] = "@"
        self.lis[self.fish._y][self.fish._x] = "-"
        
        for row in self.lis :
            for ch in row:
                print(ch, end="")
            print()


if __name__ == '__main__':
    Game()