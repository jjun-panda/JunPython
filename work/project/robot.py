from tkinter import END, Canvas, Frame, PanedWindow, PhotoImage, Tk
from tkinter.ttk import Label, Button, Entry
import tkinter.font as tkFont

class Product:
    def __init__(self, name, brand, price, image):
        self.name = name
        self.brand = brand
        self.price = price
        self.image = image

class ShoppingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ROBOT AI SYSTEM")

        # 지정스타일
        fontStyle = tkFont.Font(family="Pretendard Variable", size=32)
        fontStyle1 = tkFont.Font(family="Pretendard Variable", size=24)
        fontStyle2 = tkFont.Font(family="Pretendard Variable", size=16)

        # 제품 목록 프레임
        product_frame = Frame(self.master)
        product_frame.pack(side="left", padx=40, pady=40, fill="y")

        # 제품 목록 라벨
        lbl_title = Label(leftFrame, text="ROBOT AI SYSTEM", font=fontStyle)
        #lbl_title.pack(side="bottom", anchor="center")
        lbl_title.place(x=40, y=60, anchor='w')

        # 검색 버튼
        search_btn = Button(rightFrame, text="검색", command=self.search_product)
        search_btn.pack(side="right", padx=40, pady=40, fill="y")

        # 검색 엔트리
        search_entry = Entry(rightFrame, font=fontStyle2)
        search_entry.pack(side="right", padx=40, pady=40, fill="y")

        # 제품 리스트
        self.products = [
            Product("웨어러블", "현대로템", 1200000, "icon1.png"),
            Product("로봇암", "두산로보틱스", 1500000, "icon2.png"),
            Product("산업용", "현대로보틱스", 2500000, "icon3.png"),
            Product("청소용", "비죠아", 2000000, "icon4.png"),
            Product("공간용", "지우개", 300000, "icon5.png")
        ]
        
        # 제품 목록 캔버스
        self.product_canvas = Canvas(product_frame, width=720, height=720, bd=0, highlightthickness=0)
        self.product_canvas.pack()

        # 제품 목록
        self.product_images = []
        for i, product in enumerate(self.products):
            row, col = divmod(i, 4) # 행과 열 계산
            image = PhotoImage(file=product.image)
            self.product_images.append(image)
            # 이미지와 제품명을 하나의 버튼으로 묶어 생성
            button = Button(self.product_canvas, image=image, text=f"{product.name}\n{product.brand}", compound="top", command=lambda product=product: self.show_product_info(product))
            button.grid(row=row, column=col)
            self.product_canvas.create_window(col*185+80, row*180+100, window=button)

        # 제품 추가 버튼
        add_btn = Button(bottomFrame, text="제품 추가", command=self.add_product)
        add_btn.pack(side="right", padx=30, pady=30, fill="y")
    
    def add_product(self):
        # 제품 추가 창
        add_window = Tk()
        add_window.title("제품 추가")
        add_window.geometry("300x200")

        # 제품 이름 입력
        name_lbl = Label(add_window, text="제품 이름")
        name_lbl.pack()
        name_entry = Entry(add_window)
        name_entry.pack()

        # 제품 브랜드 입력
        brand_lbl = Label(add_window, text="제조사")
        brand_lbl.pack()
        brand_entry = Entry(add_window)
        brand_entry.pack()

        # 제품 가격 입력
        price_lbl = Label(add_window, text="가격")
        price_lbl.pack()
        price_entry = Entry(add_window)
        price_entry.pack()

        # 제품 이미지 파일명 입력
        image_lbl = Label(add_window, text="이미지 파일명")
        image_lbl.pack()
        image_entry = Entry(add_window)
        image_entry.pack()

        # 추가 버튼
        add_btn = Button(add_window, text="추가", command=lambda: self.add_product_to_list(name_entry.get(), brand_entry.get(), price_entry.get(), image_entry.get(), add_window))
        add_btn.pack()

    # 제품 추가
    def add_product_to_list(self, name, brand, price, image, add_window):
        product = Product(name, brand, price, image)
        self.products.append(product)
        self.show_product_list()
        add_window.destroy()

    # 제품 클릭시 콘솔에 출력할 내용
    def show_product_info(self, product):
        print(f"{product.name}({product.brand})를 선택하셨습니다")

    def search_product(self):
        search_query = self.search_entry.get()
        if search_query:
            results = [product for product in self.products if search_query.lower() in product.name.lower()]
            if results:
                self.product_canvas.delete("all")
                self.product_images.clear()
                for i, product in enumerate(results):
                    row, col = divmod(i, 4)
                    image = PhotoImage(file=product.image)
                    self.product_images.append(image)
                    button = Button(self.product_canvas, image=image, text=f"{product.name}\n{product.brand}\n{product.price}원", compound="top", command=lambda product=product: self.show_product_info(product))
                    button.grid(row=row, column=col)
                    self.product_canvas.create_window(col*185+84, row*250+100, window=button)
            else:
                print("No results found.")



mac = Tk()
mac.geometry("800x800")
mac.title("Robot Sol System")

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(mac)
leftFrame.pack(side='left')
leftFrame.config(width=400, height=120, background="#00c09f")

rightFrame = Frame(mac)
rightFrame.pack(side='right')
rightFrame.config(width=400, height=120, background="green")


panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(mac)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=30, background="blue")


if __name__ == "__main__":
    app = ShoppingApp(mac)
    mac.mainloop()
