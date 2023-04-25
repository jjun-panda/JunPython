from tkinter import Tk
from tkinter.ttk import Label, Button

mac = Tk()
mac.geometry("400x200+200+200")
lbl = Label(mac, text = "결제 완료되었습니다!")
btn1 = Button(mac, text = "확인")
btn2 = Button(mac, text = "취소")

lbl.pack()
btn1.pack()
btn2.pack()

if __name__ == "__main__":
    mac.mainloop()