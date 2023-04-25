from tkinter import*
from tkinter import messagebox
import random


next_move = None
next_move2 = None
def clicked():
    window.after_cancel(next_move)
    messagebox.showinfo("미션 성공","모기 잘 잡는군요!")
    messagebox.showinfo("다음단계","다음단계로 넘어갑니다")
    btn_move2()

def clicked2():
    window.after_cancel(next_move2)
    messagebox.showinfo("미션 성공", "와우! 멋있어요!")
    window.quit()#성공하고나서 화면 닫기

def btn_move():
    global next_move#모르겟다.. 왜 여길 넣어야했을까?
    new_x = random.randint(50,750)#화면 가로세로 모기나타나는 랜덤
    new_y = random.randint(50,750)
    dalay = random.randint(2000,2000)#모기 속도
    button.place(x = new_x, y= new_y)
    next_move = window.after(dalay, btn_move)

def btn_move2():
    global next_move2#모르겟다.. 왜 여길 넣어야했을까?
    new_x = random.randint(50,750)#화면 가로세로 모기나타나는 랜덤
    new_y = random.randint(50,750)
    dalay = random.randint(2000,2000)#모기 속도
    button.place(x = new_x, y= new_y)
    next_move2 = window.after(dalay, btn_move2)

window = Tk()#맨처음에 필요한 것들 넣는거임.
window.title("초 쉬운 미니 클릭 게임")
window.geometry("800x800")
# window.resizable(False,False)

img=PhotoImage(file="mm.png")#넣을 이미지  파일
button=Button(window, image=img, command=clicked)#이미지파일 버튼으로 변경
button.place(x=250,y=250)


img1=PhotoImage(file="img00.png")#넣을 이미지  파일
button=Button(window, image=img1, command=clicked)#이미지파일 버튼으로 변경
button.place(x=250,y=250)

btn_move()#화면에 나오게 하는건 이것.
btn_move2()


if __name__ == '__main__':
    window.mainloop()