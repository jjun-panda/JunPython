from tkinter import Tk, PanedWindow, Menu, LabelFrame
from tkinter.ttk import Label, Button, Entry

mac = Tk()
mac.geometry("400x200+200+200")

menu_area = Menu()
mac.configure(menu=menu_area)

menu1 = Menu(menu_area)
menu1.add_command(label="New...")
menu_area.add_cascade(label="file", menu=menu1)

label_frame = LabelFrame(mac, text='label frame')
label_frame.grid(row=0, column=0, padx=5, pady=5)

lbl_name = Label(label_frame, text="성명 : ")
lbl_phone = Label(label_frame, text="번호 : ")
lbl_email = Label(label_frame, text="이메일 : ")

entry_name = Entry(label_frame)
entry_phone = Entry(label_frame)
entry_email = Entry(label_frame)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, padx=5, pady=5)
lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1, padx=5, pady=5)
lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1, padx=5, pady=5)

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_1 = Button(panedwindow, text="확인")
btn_2 = Button(panedwindow, text="취소", )

panedwindow.add(btn_1)
panedwindow.add(btn_2)

if __name__ == '__main__' :
    mac.mainloop()