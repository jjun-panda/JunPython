class Music :
    def __init__(self, track, title, singer):
        self.track = track
        self.title = title
        self.singer = singer

    def play(self):
        print(f"{self.track}번 트랙 {self.singer}의 {self.title} 실행중입니다.")

    def list(self):
        return f"[{self.track}] {self.singer} | {self.title}"

class MusicPlayer :
    def __init__(self):
        self.number = 1
        self.musiclist = []
        
    def music_paly(self, music):
        self.musiclist.append(music)

    # 추가
    def input(self):
        print("새 노래를 계속 입력해주세요. (종료는 '그만'입력!)")
        while True:
            track = self.number
            self.number += 1
            title = input("곡목 입력>> ")
            if title == "그만" :
                print("곡 추가 기능을 마칩니다.")
                break
            singer = input("가수 입력>> ")
            music = Music(track, title, singer)
            self.musiclist.append(music)

    # 제거
    def remove(self, idx):
        if idx < len(self.musiclist):
            dele = self.musiclist[idx-1] # -1 뺴야한다.
            print(f"{dele.track}번 트랙 {dele.singer}의 {dele.title} 삭제했습니다.")
            del self.musiclist[idx-1]
        else :
            print("삭제 할 음악이 없습니다")

    # 전곡 실행
    def play_all(self):
        for music in self.musiclist : 
            music.play()
    

m_play = MusicPlayer()
while True:
    print("::Music Player::")
    for music in m_play.musiclist : 
        print(music.list())
    no = int(input("(1)추가 (2)제거 (3)전곡 실행 (4)종료 >> "))
    if no == 1:
        m_play.input()
        
    elif no == 2:
        id_num = int(input("삭제할 번호 입력해주세요>> "))
        m_play.remove(id_num)

    elif no == 3:
        m_play.play_all()

    elif no == 4:
        print("뮤직 플레이어 종료!")
        break