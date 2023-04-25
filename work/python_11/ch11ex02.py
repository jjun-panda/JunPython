from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

mac = Tk()
mac.geometry("400x100+200+200")
lbl = Label(mac, text="설명: ")
entry = Entry(mac)
btn = Button(mac, text="확인")

lbl.pack()
entry.pack()
btn.pack()

if __name__ == '__main__' :
    mac.mainloop()