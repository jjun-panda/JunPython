# from tkinter import Tk
from tkinter import Tk, Label, Button

mac = Tk()
mac.geometry("400x250+200+200")

top_label = Label(mac, text="top", background="Green")
top_label.pack(side="top", fill="x")

left_label = Label(mac, text="left", background="#9f00c0")
left_label.pack(side="left", fill="y")

bottom_label = Label(mac, text="bottom", background="#009fc0")
bottom_label.pack(side="bottom", fill="x")

right_label = Label(mac, text="right", background="#d1d1d1")
right_label.pack(side="right", fill="y")

btn = Button(mac, text = "확인")
btn.pack(side= "bottom", anchor="e")

if __name__ == '__main__' :
    mac.mainloop()