
class TV :
    volume = 5
    power = False
    model = None

    def __init__(self, model):
        self.model = model
        print(f"{self.model}TV 생성")

    def powerOn(self):
        if self.power == False :
            self.power = True
            print(f"{self.model}TV 켜기")
        else :
            print(f"{self.model}TV 이미 켠 상태입니다.")

    def volumeUp(self):
        self.volume += 1
        print(f"{self.model}TV 소리 키우기 volume: {self.volume}")

    def volumeDown(self):
        self.volume -= 1
        print(f"{self.model}TV 소리 줄이기 volume: {self.volume}")


    def powerOff(self):
        if self.power == True :
            self.power = False
            print(f"{self.model}TV 끄기")
        else :
            print(f"{self.model}TV 이미 끈 상태입니다.")

samsungTV = TV("삼성")
samsungTV.powerOn()
samsungTV.volumeUp()

samsungTV.volumeDown()
samsungTV.powerOff()
samsungTV.powerOff()
samsungTV.powerOn()
samsungTV.powerOff()