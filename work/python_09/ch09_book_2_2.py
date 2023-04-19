from turtle import *

color('#191919', '#00c09f')
begin_fill() # 도형 안에 색을 칠하기 위해 준비
pensize(2) # 선의 굵기
while True:
    forward(300) # 선의 길이
    left(150) # 왼쪽방향으로 그리기
    if abs(pos()) < 1:
        break
end_fill()
done() # 완료하면 닫지 않고 그대로 두기
