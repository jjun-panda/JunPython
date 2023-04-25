from tkinter import Tk, PanedWindow 
from tkinter.ttk import Label, Button, Entry

mac = Tk()
mac.geometry("400x150+200+200")

lbl_name = Label(mac, text="성명 : ")
lbl_phone = Label(mac, text="번호 : ")
lbl_email = Label(mac, text="이메일 : ")

entry_name = Entry(mac)
entry_phone = Entry(mac)
entry_email = Entry(mac, width=100)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1)
lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=3, column=0, columnspan=2)

btn_1 = Button(panedwindow, text="확인")
btn_2 = Button(panedwindow, text="취소", )

panedwindow.add(btn_1)
panedwindow.add(btn_2)

if __name__ == '__main__' :
    mac.mainloop()