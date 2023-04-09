lis = [
    {'score':100, "rank":1},
    {'score':90, "rank":1},
    {'score':83, "rank":1},
    {'score':85, "rank":1},
    {'score':76, "rank":1},
    {'score':10, "rank":1},
    {'score':83, "rank":1},
]

# lis를 반복한다.
# score를 비교한다.
# 다른 요소의 score가 현재요소의 score가 크면 rank 증가

i = 0
while i < len(lis):
    lis[i]["rank"] = 1
    j = 0
    while j < len(lis):
        if lis[i]['score'] < lis[j]['score']:
            lis[i]["rank"] = lis[i]["rank"] + 1
        j += 1
    i += 1

#  반복문을 이용한 정렬
# 선택 정렬이 제일 쉬움
i = 0
while i < len(lis)-1:
    j = i+1
    print(i)
    while j < len(lis):
        if lis[i]['score'] < lis[j]['score'] :
            # 파이썬에서는 튜플을 이용한 swqp 가능
            (lis[i], lis[j]) = (lis[j], lis[i])
        j += 1
    i += 1
for std in lis:
    print(std)