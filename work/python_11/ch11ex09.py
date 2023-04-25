from tkinter import Tk, Label

x = 150
y = 100

def mouseEvtHandler(event):
    global x, y
    x, y = (event.x, event.y)
    print("{}, {}".format(x, y))
    lbl.place(x=x, y=y)

def scroll(event):
    global y
    print(event.delta)
    if event.delta == -120 :
        y += 10
    if event.delta == 120 :
        y -= 10
    lbl.place(x=x, y=y)

mac = Tk()
mac.geometry("400x200+200+200")

lbl = Label(mac, text="자연인")
lbl.place(x=150, y=100)

mac.bind("<B1-Motion>", mouseEvtHandler)
mac.bind("<MouseWheel>", scroll)

if __name__ == "__main__":
    mac.mainloop()
