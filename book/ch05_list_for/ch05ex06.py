#같은 요소값을 한꺼번에 제거
li=[1,1,1,1,2,2,2,2,3,3,3,4,4,4,4]
# remove()함수는 요소 중 맨 처음에 위치한 요소 하나만 제거한다.
li.remove(2)
print(li)

# 리스트에 있는 같은 요소를 한꺼번에 지우기 위해서 반복문 사용.
while 3 in li :
    li.remove(3)
print(li)