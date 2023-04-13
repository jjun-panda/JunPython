class Car :
    def __init__(self, name, year, brand) :
        self.name = name
        self.year = year
        self.brand = brand
        self.speed = 50

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        self.speed -= 10

    def run(self):
        print(f"{self.brand} {self.name}가 {self.year}년이 {self.speed}킬로로 달린다.")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} {self.name} 정지!")

sonata = Car("SONATA", 2019, "HYUNDAI")
sonata.run()

sonata.speed_up()
sonata.run()

sonata.speed_up()
sonata.run()

sonata.speed_down()
sonata.speed_down()
sonata.run()

sonata.stop()