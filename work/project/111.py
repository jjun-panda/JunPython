from tkinter import END, Frame, Tk
from tkinter.ttk import Label, Button, Entry

root = Tk()
root.geometry("600x400+100+100")

class Product:
    def __init__(self, name, brand, price, image):
        self.name = name
        self.brand = brand
        self.price = price
        self.image = image

class ShoppingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Product")

        # 제품 리스트
        self.products = [
            Product("웨어러블", "현대로템", 1200000, "wearable.png"),
            Product("로봇암", "두산로보틱스", 1500000, "robotarm.png"),
            Product("산업용", "현대로보틱스", 2500000, "industry.png"),
            Product("청소용", "비죠아", 2000000, "cleaning.png"),
            Product("공간용", "지우개", 300000, "space.png")
        ]

        # 제품 목록 프레임
        product_frame = Frame(self.master)
        product_frame.pack(side="left", padx=10, pady=10, fill="y")

        # 제품 목록 라벨
        Label(product_frame, text="제품 목록", font=("Pretendard Variable", 16)).pack()

        # 제품 목록 캔버스
        self.product_canvas = Canvas(product_frame, width=200, height=300)
        self.product_canvas.pack(padx=10, pady=10)

        # 제품 목록에 제품 추가
        for i, product in enumerate(self.products):
            image = PhotoImage(file=product.image)
            self.product_canvas.create_image(100, (i * 70) + 50, image=image)
            self.product_canvas.tag_bind(f"product{i}", "<Button-1>", lambda event, product=product: self.show_product_info(product))
            self.product_canvas.create_text(100, (i * 70) + 120, text=f"{product.name} | {product.brand} | {product.price}원", font=("Pretendard Variable", 12), tags=f"product{i}")

    # 제품 클릭시 실행될 함수
    def show_product_info(self, product):
        print(f"{product.name} ({product.brand}) - {product.price}원")

if __name__ == "__main__":
    app = ShoppingApp(root)
    root.mainloop()
