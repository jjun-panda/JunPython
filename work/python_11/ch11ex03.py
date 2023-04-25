from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

mac = Tk()
mac.geometry("400x250+200+200")
lbl_name = Label(mac, text="성명: ")
lbl_phone = Label(mac, text="번호: ")
lbl_email = Label(mac, text="이메일: ")

entry_name = Entry(mac)
entry_phone = Entry(mac)
entry_email = Entry(mac)

btn_1 = Button(mac, text="확인")
btn_2 = Button(mac, text="취소")

lbl_name.pack()
entry_name.pack()
lbl_phone.pack()
entry_phone.pack()
lbl_email.pack()
entry_email.pack()
btn_1.pack()
btn_2.pack()

if __name__ == '__main__' :
    mac.mainloop()