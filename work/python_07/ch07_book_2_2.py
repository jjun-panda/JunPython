class Music :
    def __init__(self, track, title, singer):
        self.track = track
        self.title = title
        self.singer = singer

    def play(self):
        print(f"{self.track}번 트랙 {self.singer}의 {self.title} 실행중입니다.")

music = Music(1, "Festival", "엄정화")
music.play()