class TV :
    # 생성자, 필드, 메소드를 구현 하시오.
    name = None
    channel = 11
    speaker = None

    def __init__(self, name, speaker):
        self.name = name
        self.speaker = speaker
        print(f"{self.name} TV 생성")


    def powerOn(self):
        print(f"{self.name} TV 켜기")
        
        
    def powerOff(self):
        print(f"{self.name} TV 끄기")
        
        
    def volumeUp(self):
        self.speaker.volumeUp()

    def volumeDown(self):
        self.speaker.volumeDown()


class Speaker :
    volume = 3
    name = None

    def __init__(self, name):
        self.name = name


    def volumeUp(self):
        self.volume += 1
        print(f"{self.name} 소리 키우기 volume: {self.volume}")


    def volumeDown(self):
        self.volume -= 1
        print(f"{self.name} 소리 줄이기기 volume:  {self.volume}")


samsungTV = TV("삼성", Speaker("Sony"))

samsungTV.powerOn()
samsungTV.volumeUp()
samsungTV.volumeDown()
samsungTV.powerOff()