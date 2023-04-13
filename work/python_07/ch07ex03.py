import math

class Circle :
    def __init__(self, r) :
        self.r = r
        self.mkArea()
        self.mkLine()
    
    def mkArea(self) :
        self.area = math.pi * self.r**2 # ** = 제곱의미 // 파이 * 길이의 2제곱

    def mkLine(self) :
        self.line = 2 * math.pi * self.r # 2 * 파이 * 길이

    def __str__(self) :
        return "원의 면적:%.3f, 원의 둘레길이:%.3f" %(self.area, self.line)
    
output = Circle(10)
print(output)