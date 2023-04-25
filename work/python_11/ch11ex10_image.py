from tkinter import Tk, PhotoImage, Label, Button

def changed(newImg) :
    imgLabel.configure(image = newImg, width=800, height=800)
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
mac.geometry("800x800+100+100")

image1 = PhotoImage(file = "logo_1.png")
imgLabel1 = Label(mac, image=image1, width=200, height=200)
imgLabel1.grid(row=0, column=0)

image2 = PhotoImage(file = "logo_2.png")
imgLabel2 = Label(mac, image=image2, width=200, height=200)
imgLabel2.grid(row=0, column=1)

image3 = PhotoImage(file = "logo_3.png")
imgLabel3 = Label(mac, image=image3, width=200, height=200)
imgLabel3.grid(row=0, column=2)

image4 = PhotoImage(file = "logo_1.png")
imgLabel4 = Label(mac, image=image4, width=200, height=200)
imgLabel4.grid(row=1, column=0)

image5 = PhotoImage(file = "logo_2.png")
imgLabel5 = Label(mac, image=image5, width=200, height=200)
imgLabel5.grid(row=1, column=1)


if __name__ == "__main__":
    mac.mainloop()