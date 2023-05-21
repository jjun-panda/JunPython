from tkinter import PhotoImage, Tk
from tkinter.ttk import Label, Button
import winsound

# 새로운 창에 이미지를 띄우는 함수
def img_win() :

    # 새로운 창에서 알람 종료 버튼 클릭 시 실행되는 함수
    def alarm_destroy():
        new_win2.destroy()

        # 노래 정지
        winsound.PlaySound(None, winsound.SND_PURGE)

    # 이미지와 알람 종료 버튼을 띄울 새 창 생성
    new_win2 = Tk()
    # 전체 화면
    new_win2.attributes("-fullscreen", 1)

    # 메인 창이 아닌 새 창이 필요할 경우 반드시 master로 어떤 창에서 이미지가 뜰 것인지를 명시해줘야 함
    image = PhotoImage(file='timer.PNG', master=new_win2)
    imgLabel = Label(new_win2, image=image)
    imgLabel.grid(row=0, padx=230, pady=100)

    quit_btn = Button(new_win2, text='알람 종료', width=50, command=alarm_destroy)
    quit_btn.grid(padx=230)

    new_win2.mainloop()