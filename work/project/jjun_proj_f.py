
from tkinter import Frame, Label, PanedWindow, Tk, Canvas, Entry, Text, Button, PhotoImage

mac = Tk()

# 창 크기 설정
mac.geometry("800x800")
# 창 제목 설정
mac.title("Robot Sol System")
# 창 배경색 설정
bg_img = PhotoImage(file="robot_bg.png")
bg_label = Label(mac, image=bg_img)
bg_label.place(x=0, y=0)

canvas = Canvas(
    mac,
    bg = "#00c09f",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    40.0,
    160.0,
    205.0,
    325.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    40.0,
    433.0,
    205.0,
    598.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    225.0,
    160.0,
    390.0,
    325.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    410.0,
    28.0,
    760.0,
    88.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    225.0,
    433.0,
    390.0,
    598.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    410.0,
    160.0,
    575.0,
    325.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    410.0,
    433.0,
    575.0,
    598.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    595.0,
    160.0,
    760.0,
    325.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    595.0,
    433.0,
    760.0,
    598.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    40.0,
    32.0,
    anchor="nw",
    text="ROBOT AI SYSTEM",
    fill="#1E1E1E",
    font=("Arial-BoldMT", int(32.0))
)

canvas.create_rectangle(
    40.0,
    333.0,
    205.0,
    387.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    40.0,
    606.0,
    205.0,
    660.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    410.0,
    333.0,
    575.0,
    387.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    410.0,
    606.0,
    575.0,
    660.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    225.0,
    333.0,
    390.0,
    387.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    225.0,
    606.0,
    390.0,
    660.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    595.0,
    333.0,
    760.0,
    387.0,
    fill="#000000",
    outline="")

canvas.create_text(
    595.0,
    606.0,
    anchor="nw",
    text="Robot AI System",
    fill="#1E1E1E",
    font=("Arial-BoldMT", int(13.0))
)

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
