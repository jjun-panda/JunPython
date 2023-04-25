from tkinter import Frame, Listbox, PhotoImage, Tk, Label, Button, Entry
import tkinter.font as tkFont

# tkinter 객체 생성
root = Tk()

# 창 크기 설정
root.geometry("800x800")

# 창 제목 설정
root.title("My Shopping App")

# 창 크기 조절 여부 설정
root.resizable(False, False)

# 창 배경색 설정
root.configure(background= "#F5F5F5")

# 폰트 스타일 설정
fontStyle = tkFont.Font(family="Pretendard Variable", size=16)

# 상단 프레임 생성
topFrame = Frame(root)
topFrame.pack(side='top')

# 상단 라벨 생성 및 설정
lbl_title = Label(topFrame, text="My Shopping App", font=fontStyle, foreground="#000000", anchor="center", bg = "#F5F5F5", width=800)
lbl_title.pack(pady=10)

# 이미지 생성
logo_image = PhotoImage(file="logo_1.png")

# 이미지를 표시할 라벨 생성 및 설정
logo_label = Label(root, image=logo_image, bg="#F5F5F5")
logo_label.pack(pady=10)

# 검색어 입력 라벨 생성 및 설정
search_label = Label(root, text="검색어 입력", font=fontStyle, bg="#F5F5F5")
search_label.pack(pady=10)

# 검색어 입력 엔트리 생성
search_entry = Entry(root, font=fontStyle, width=30)
search_entry.pack(pady=10)

# 검색 버튼 생성
search_button = Button(root, text="검색", font=fontStyle, bg="#00c09f", foreground="#FFFFFF")
search_button.pack(pady=10)

# 제품 리스트 라벨 생성 및 설정
product_label = Label(root, text="제품 리스트", font=fontStyle, bg="#F5F5F5")
product_label.pack(pady=10)

# 제품 리스트 박스 생성
product_listbox = Listbox(root, font=fontStyle, width=50, height=10)
product_listbox.pack(pady=10)

# 장바구니 라벨 생성 및 설정
cart_label = Label(root, text="장바구니", font=fontStyle, bg="#F5F5F5")
cart_label.pack(pady=10)

# 장바구니 리스트 박스 생성
cart_listbox = Listbox(root, font=fontStyle, width=50, height=10)
cart_listbox.pack(pady=10)

# 추가 버튼 생성
add_button = Button(root, text="추가", font=fontStyle, bg="#00c09f", foreground="#FFFFFF")
add_button.pack(pady=10)

# 삭제 버튼 생성
remove_button = Button(root, text="삭제", font=fontStyle, bg="#00c09f", foreground="#FFFFFF")
remove_button.pack(pady=10)

# 구매 버튼 생성
buy_button = Button(root, text="구매", font=fontStyle, bg="#00c09f", foreground="#FFFFFF")
buy_button.pack(pady=10)

# tkinter mainloop 실행
import tkinter as tk

def buy_button_clicked():
    print("Buy button clicked!")

root = tk.Tk()
root.geometry("300x200")

buy_button = tk.Button(root, text="Buy", command=buy_button_clicked)
buy_button.pack(pady=10)

root.mainloop()
