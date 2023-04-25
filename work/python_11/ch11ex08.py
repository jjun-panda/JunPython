from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

def btnEvtHandler():
    print("버튼이 클릭 되었습니다!")
    value = entry.get()
    lbl.config(text="성명: " + value)

mac = Tk()
mac.geometry("400x200+200+200")

lbl = Label(mac, text="성명 : ")
entry = Entry(mac)
btn = Button(mac, text="확인", command=btnEvtHandler)

lbl.pack()
entry.pack()
btn.pack()

if __name__ == '__main__' :
    mac.mainloop()