import turtle as t #이동과 그리기 모듈(거북이)
import random
import time


def find_card(x, y):
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx

def score_update(m):
    score_pen.clear()
    score_pen.write(f"{m} {score}점/{attempt}번 시도",False,"center")

def result(m):
    t.goto(0, -60)
    t.write("Game Over", False, "center",("",30,"bold"))


def paly(x, y):
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score

    if attempt == 12:
        result("아이고......")

    else:
        click_num += 1  # 클릭한 이미지 찾기
        card_idx = find_card(x,y)
        turtles[card_idx].shape(img_list[card_idx])

        if click_num == 1:
            first_pick = card_idx
        elif click_num == 2:
            second_pick = card_idx
            click_num = 0
            attempt += 1

            if img_list[first_pick] == img_list[second_pick]:
                score += 1
                score_update("정답")
                result("성공")
        else:
            score_update("오답")
            turtles[first_pick].shape(default_img)
            turtles[second_pick].shape(default_img)

t.bgcolor("white")#터틀모듈 에있는 그래픽 전체 핑크색으로 지정
t.setup(700,700)#그래픽 크기 가로세로 700
t.up()
t.ht()
t.goto(0,280)#이동하게 하는 명령어
t.write("카드 매칭 게임",False,"center",("",30,"bold"))#이동x 가운데정렬/글자크기 30에 굵게 센터자리

#점수 펜 객체 생성
score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(0,230)


#터틀 객체 생성
turtles = []
pos_x = [-210,-70,70,210]
pos_y = [-250,-110,30,170] #1의 위치

for x in range(4):
    for y in range(4):
        new_turtle = t. Turtle()
        new_turtle.up()
        new_turtle.color("white")
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x],pos_y[y])
        turtles.append(new_turtle)

default_img = "cor/default_img.gif"
t.addshape(default_img)

img_list = []
for i in range(8):
    img = f"cor/img{i}.gif"
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)

random.shuffle(img_list)
for i in range(16):
    turtles[i].shape(img_list[i])

time.sleep(1)

for i in range(16):
    turtles[i].shape(default_img)

t.done()