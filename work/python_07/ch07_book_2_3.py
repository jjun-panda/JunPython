class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_point(self):
        print(f"x={self.x} y={self.y}")

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

p1 = Point(10, 20)
p1.show_point()

p1.set_point(100, 200)
print(p1.get_x(), p1.get_y())