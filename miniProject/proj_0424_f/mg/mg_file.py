import time
import winsound
from tkinter import*#모듈 기능 다 사용가능 별표 잇으면 다불러오는거라고함.
from tkinter import messagebox,Label
import random




#-----------------------------------------------------------------------------------------------
next_move = None
# next_move2 =None

level = 1
#------------------------------------------------------------------------------------------------
def clicked():
    global level
    window.after_cancel(next_move)
    winsound.PlaySound('clap.wav', winsound.SND_ASYNC)
    if level == 1 :
        messagebox.showinfo("미션 성공", "고마워요!!")
        messagebox.showinfo("다음 단계", "두마리 더 잡아줘요!!")
        level = 2
        btn_move()
        winsound.PlaySound('m.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

    elif level == 2:
        messagebox.showinfo("미션 성공", "진짜 고마워요~")
        messagebox.showinfo("다음 단계", "한마리 더 남았어요!")
        level = 3
        btn_move()
        winsound.PlaySound('m.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

    elif level == 3 :
        clicked3()

# def clicked2():
#     window.after_cancel(next_move)
#     messagebox.showinfo("미션 성공", "진짜 고마워요~")
#     messagebox.showinfo("다음 단계", "한마리 더 남아있어요!")

def clicked3():
    window.after_cancel(next_move)
    messagebox.showinfo("미션 성공", "와!")
    messagebox.showinfo("미션 종료", "탁구선수로 가도 될 실력입니다.")
    window.quit()#성공하고나서 화면 닫기

#Label(window, text="1단계").pack()
def btn_move():
    global level
    global next_move#모르겟다.. 왜 여길 넣어야했을까?
    new_x = random.randint(100,700)#화면 가로세로 모기나타나는 랜덤
    new_y = random.randint(100,700)
    if level == 1 :
        print("1단계")
        dalay = random.randint(600,800)#모기 속도
    elif level == 2 :
        print("2단계")
        dalay = random.randint(400, 600)  # 모기 속도
    elif level == 3 :
        print("3단계")
        dalay = random.randint(300, 500)  # 모기 속도
    button.place(x = new_x, y= new_y)
    next_move = window.after(dalay, btn_move)

#--------------------------------------------------------------------------------------------------
window = Tk()#맨처음에 필요한 것들 넣는거임.

window.title("초 쉬운 미니 클릭 게임")
window.geometry("800x800")

# bg_img = PhotoImage(file="img01.png")
# bg_label1 = Label(window,text="1단계",image=bg_img)
# bg_label1.place(x=0, y=0)

bg_img = PhotoImage(file="img01.png")
bg_label = Label(window,image=bg_img)
bg_label.place(x=0, y=0)

img=PhotoImage(file="img02.png")#넣을 이미지  파일
button=Button(window, image=img, command=clicked, cursor="hand2")#이미지파일 버튼으로 변경
button.place(x=250,y=250)


winsound.PlaySound('m.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

btn_move()

if __name__ == '__main__':
    window.mainloop()
