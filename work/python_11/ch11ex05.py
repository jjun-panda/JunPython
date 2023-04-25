from tkinter import Tk, PanedWindow 
from tkinter.ttk import Label, Button, Entry

mac = Tk()
mac.geometry("400x100+200+200")

lbl = Label(mac, text="성명 : ")
entry = Entry(mac)

lbl.pack()
entry.pack()

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

btn_1 = Button(panedwindow, text="확인")
btn_2 = Button(panedwindow, text="취소")

panedwindow.add(btn_1)
panedwindow.add(btn_2)

if __name__ == '__main__' :
    mac.mainloop()