from turtle import Turtle

t = Turtle()
t.color("#009681")
t.pensize(5) # 선굵기
t.shape("turtle")

def moveTurtle() :
    direction = input("진행 방향 입력(Left:L 또는 Right:R) >> ")
    angle = int(input("각도 입력(정수) >>"))
    length = int(input('거리 입력(정수) >>'))

    t.left(angle) if direction == "L" else t.right(angle)
    t.forward(length)


for i in range(5) : # 최대 5번까지 진행가능
    moveTurtle()

input('Press any key to continue ...')