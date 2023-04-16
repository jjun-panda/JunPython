class Washer :
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        print(f">> {self.maker}세탁기가 {self.size}킬로의 빨래를 한다.")
        self.info()
    
    def __str__(self) :
        return f"size: {self.size}kg, maker: {self.maker}"


class LGWasher(Washer) :
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name
    
    def info(self):
        print(f"size: {self.size}kg")
        print(f"company: {self.maker}")
        print(f"name: {self.name}")

    def __str__(self):
        return super().__str__() + f", name: {self.name}"

class SamungWasher(Washer) :
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name
    
    def info(self):
        print(f"size: {self.size}")
        print(f"company: {self.maker}")
        print(f"name: {self.name}")

    def __str__(self):
        return super().__str__() + f", name: {self.name}"


lg = LGWasher(100, "LG", "돌아라")
print(lg)
lg.washing()
print()
samsung = SamungWasher(90, "Samsung", " 도돌이")
print(samsung)
samsung.washing()