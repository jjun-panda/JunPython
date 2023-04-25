from tkinter import Frame, PhotoImage, Tk, PanedWindow, Label, Button, Entry
import tkinter.font as tkFont

# Tkinter 객체 생성
mac = Tk()

# 창 크기 설정
mac.geometry("800x800")

# 창 제목 설정
mac.title("Robot Sol System")

# 창 크기 조절 여부 설정
# mac.resizable(False, False)

# 창 배경색 설정
mac.configure(background= "#00c09f")
bg_img = PhotoImage(file="robot_bg.png")
bg_label = Label(mac, image=bg_img)
bg_label.place(x=0, y=0)

# 상단 프레임 생성
topFrame = Frame(mac)
topFrame.pack(side='top')

# 폰트 스타일 설정
fontStyle = tkFont.Font(family="Pretendard Variable", size=40)

# 상단 레이블 생성 및 설정
lbl_title = Label(topFrame, text="폰트 확인", font=fontStyle, foreground="#ffffff", anchor="center", bg = "#009681", width=400)
lbl_title.pack()

# 이미지 생성 및 버튼 생성 후 추가
img = PhotoImage(file="logo_1.png")
btn = Button(mac, text="Click me", image=img, width=160, height=160, border=0, compound="top", command=lambda: print("Button clicked"))
btn.pack(side="left")
btn1 = Button(mac, text="Click me", image=img, width=160, height=160, border=0, compound="top", command=lambda: print("Button clicked"))
btn1.pack(side="left")
btn2 = Button(mac, text="Click me", image=img, width=160, height=160, border=0, compound="top", command=lambda: print("Button clicked"))
btn2.pack(side="left")

# 하단 프레임 생성
bottomFrame = Frame(mac)
bottomFrame.pack(side='bottom')

# PanedWindow 생성 및 설정
panedwindow=PanedWindow(bottomFrame, relief="raised", bd=0, bg="#00c09f")
panedwindow.pack()

# 하단 버튼 생성 및 추가
btn_output = Button(panedwindow, fg="#009681", highlightbackground="#00c09f", text="전체보기")
btn_input = Button(panedwindow, fg="#009681", highlightbackground="#00c09f", text="입력")
btn_search = Button(panedwindow, fg="#009681", highlightbackground="#00c09f", text="검색")
btn_modify = Button(panedwindow, fg="#009681",  highlightbackground="#00c09f", text="수정")
btn_delete = Button(panedwindow, fg="#009681",  highlightbackground="#00c09f", text="삭제")
btn_backup = Button(panedwindow, fg="#009681",  highlightbackground="#00c09f", text="파일백업")


panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
panedwindow.add(btn_backup)

if __name__ == '__main__' :
    mac.mainloop()