check = "y"
while check == 'y' :
    name = input('성명 입력>> ')
    maj = input('전공 입력>> ')
    print(name+'님의 전공은 '+maj+' 입니다.')
    
    check = input('계속 하시겠습니까? (y 또는 n 입력해주세요)')
    while not (check in['y','n']) :
        print('y 또는 n 만 입력해주세요')
        check = input('계속 하시겠습니까? (y 또는 n 입력해주세요)')
    if check == 'n' : break

print('감사합니다.')