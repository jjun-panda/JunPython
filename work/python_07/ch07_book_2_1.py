class Washer :
    def __init__(self, maker, brand, weight):
        self.maker = maker
        self.brand = brand
        self.weight = weight

    def washing(self) :
        print(f"{self.maker} {self.brand} 세탁기가 {self.weight}킬로그램의 빨래를 합니다.")


washer = Washer("LG", "트롬", 65)
washer.washing()
