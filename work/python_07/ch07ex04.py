class haha :
    def __init__(self, s, b) :
        self.s = s
        self.b = b
    
    def haha(self):
        data()
        print(f"{self.b}세탁기가 {self.s}kg 세탁하고 있습니다.")
        print("{}세탁기가 {}kg 세탁하고 있습니다.".format(self.b, self.s))

def data() :
    print("세탁기 투입!")

haha = haha(10, "samsung")
haha.haha()