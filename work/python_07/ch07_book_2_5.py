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
    
class Point3D(Point) : # 부모클래스에 Point 넣고, super()입력해야 된다
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show_point(self):
        print(f"x={self.x} y={self.y} z={self.z}")

    def set_point(self, x, y, z):
        super().set_point(x, y)
        self.z = z

    def get_x(self):
        return  self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z

p3d = Point3D(10, 20, 30)
p3d.show_point()
p3d.set_point(100,200,300)
print(p3d.get_x(), p3d.get_y(), p3d.get_z())