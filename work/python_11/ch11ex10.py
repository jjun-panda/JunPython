from tkinter import Tk, PhotoImage, Label, Button

def changed(newImg) :
    imgLabel.configure(image = newImg, width=400, height=350)
    imgLabel.image=newImg

def img1() :
    newImg = PhotoImage(file="logo_1.png")
    changed(newImg)

def img2() :
    newImg = PhotoImage(file="logo_2.png")
    changed(newImg)

def img3() :
    newImg = PhotoImage(file="logo_3.png")
    changed(newImg)

mac = Tk()
mac.geometry("400x400+100+100")

image = PhotoImage(file = "logo_1.png")
imgLabel = Label(mac, image=image, width=400, height=350)

btn_1 = Button(mac, text="logo_1", command=img1)
btn_2 = Button(mac, text="logo_2", command=img2)
btn_3 = Button(mac, text="logo_3", command=img3)


imgLabel.grid(row=0, column=0, columnspan=3)
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

if __name__ == "__main__":
    mac.mainloop()