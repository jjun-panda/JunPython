# set을 사용하지 않고 lotto번호 생성기 구현
import random

lotto = []
size = 6

while len(lotto) < size:
    num = random.randint(1,6)
    if not num in lotto:
        lotto.append(num)

lotto.sort()

print(lotto)