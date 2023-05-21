from tkinter import END, INSERT, Button, Entry, Frame, Label, PhotoImage, Text, Tk
from tkinter import messagebox, PanedWindow
from pygame import mixer

filename = '1234.mp3'
mixer.init()
mixer.music.load(filename)
mixer.music.play(-1)


class AddressBook:
    def __init__(self, master):
        self.master = master
        self.master.title("주소록")
        self.master.geometry("600x500+100+100")

        self.frame1 = Frame(self.master)
        self.frame1.pack()

        panedwindow = PanedWindow(relief="raised", bd=0)
        panedwindow.pack(expand=True)

        self.fontstyle = Tk.font=("강원교육튼튼", 16)

        self.label1 = Label(self.frame1, text="이름", font=self.fontstyle)
        self.label1.grid(row=0, column=0)

        self.entry1 = Entry(self.frame1, width=30)
        self.entry1.grid(row=0, column=1)

        self.label2 = Label(self.frame1, text="전화번호", font=self.fontstyle)
        self.label2.grid(row=2, column=0)

        self.entry2 = Entry(self.frame1, width=30)
        self.entry2.grid(row=2, column=1)

        self.button1 = Button(panedwindow, text="입력", command=self.insert,font=self.fontstyle)
        self.button2 = Button(panedwindow, text="출력", command=self.display,font=self.fontstyle)
        self.button3 = Button(panedwindow, text="수정", command=self.update,font=self.fontstyle)
        self.button4 = Button(panedwindow, text="삭제", command=self.delete,font=self.fontstyle)
        self.button5 = Button(panedwindow, text="종료", command=self.quit,font=self.fontstyle)

        panedwindow.add(self.button1)
        panedwindow.add(self.button2)
        panedwindow.add(self.button3)
        panedwindow.add(self.button4)
        panedwindow.add(self.button5)

        self.frame2 = Frame(self.master)
        self.frame2.pack()

        self.text = Text(self.frame2, width=50, height=16, font=self.fontstyle)
        self.text.pack()

        self.book = []

    def insert(self):
        name = self.entry1.get()
        phone = self.entry2.get()
        if name and phone:
            self.book.append({"name": name, "phone": phone})
            messagebox.showinfo("주소록", "성공적으로 입력되었습니다.")
        else:
            messagebox.showwarning("주소록", "이름과 전화번호를 입력하세요.")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)

    def display(self):
        self.text.delete(1.0, END)
        if self.book:
            for i, entry in enumerate(self.book):
                self.text.insert(END, f"{i+1}. 이름: {entry['name']}, 전화번호: {entry['phone']}\n")
        else:
            self.text.insert(END, "주소록이 비어 있습니다.\n")

    def update(self):
        index = self.text.index(INSERT).split(".")[0]
        if self.book:
            if int(index) <= len(self.book):
                name = self.entry1.get()
                phone = self.entry2.get()
                if name and phone:
                    self.book[int(index)-1] = {"name": name, "phone": phone}
                    messagebox.showinfo("주소록", "성공적으로 수정되었습니다.")
                else:
                    messagebox.showwarning("주소록", "이름과 전화번호를 입력하세요.")
                self.entry1.delete(0, END)
                self.entry2.delete(0, END)
            else:
                messagebox.showwarning("주소록", "수정할 항목을 선택하세요.")
        else:
            messagebox.showwarning("주소록", "주소록이 비어 있습니다.")

    def delete(self):
        index = self.text.index(INSERT).split(".")[0]
        if self.book:
            if int(index) <= len(self.book):
                self.book.pop(int(index) - 1)
                messagebox.showinfo("주소록", "성공적으로 삭제되었습니다.")
            else:
                messagebox.showwarning("주소록", "삭제할 항목을 선택하세요.")
        else:
            messagebox.showwarning("주소록", "주소록이 비어 있습니다.")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)

    def quit(self):
        if messagebox.askyesno("주소록", "종료하시겠습니까?"):
            self.master.destroy()

root = Tk()
root.title("주소록")
root.geometry("800x800")
bg_img = PhotoImage(file="planet.png", master=root)
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0)

if __name__ == "__main__":
    app = AddressBook(root)
    root.mainloop()