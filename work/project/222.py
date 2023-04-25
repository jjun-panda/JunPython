import tkinter as tk
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('robot_products.db')
c = conn.cursor()

# 제품 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS robot_products
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              manufacturer TEXT NOT NULL,
              model TEXT NOT NULL,
              price REAL NOT NULL)''')
conn.commit()

# GUI 생성
mac = tk.Tk()
mac.title("로봇 제품 관리 시스템")

# 라벨 및 입력 상자 생성
tk.Label(mac, text="제품 이름").grid(row=0)
name_entry = tk.Entry(mac)
name_entry.grid(row=0, column=1)

tk.Label(mac, text="제조사").grid(row=1)
manufacturer_entry = tk.Entry(mac)
manufacturer_entry.grid(row=1, column=1)

tk.Label(mac, text="모델").grid(row=2)
model_entry = tk.Entry(mac)
model_entry.grid(row=2, column=1)

tk.Label(mac, text="가격").grid(row=3)
price_entry = tk.Entry(mac)
price_entry.grid(row=3, column=1)

# 제품 추가 함수
def add_product():
    name = name_entry.get()
    manufacturer = manufacturer_entry.get()
    model = model_entry.get()
    price = price_entry.get()

    # 데이터베이스에 새로운 제품 추가
    c.execute("INSERT INTO robot_products VALUES (?, ?, ?, ?)", (name, manufacturer, model, price))
    conn.commit()

    # 입력 상자 초기화
    name_entry.delete(0, tk.END)
    manufacturer_entry.delete(0, tk.END)
    model_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    # 제품 목록 표시
    show_products()

# 제품 수정 함수
def update_product():
    id = id_entry.get()
    name = name_entry.get()
    manufacturer = manufacturer_entry.get()
    model = model_entry.get()
    price = price_entry.get()

    # 데이터베이스에서 선택한 제품 수정
    c.execute("UPDATE robot_products SET name=?, manufacturer=?, model=?, price=? WHERE id=?", (name, manufacturer, model, price, id))
    conn.commit()

    # 입력 상자 초기화
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    manufacturer_entry.delete(0, tk.END)
    model_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    # 제품 목록 표시
    show_products()

# 제품 삭제 함수
def delete_product():
    id = id_entry.get()

    # 데이터베이스에서 선택한 제품 삭제
    c.execute("DELETE FROM robot_products WHERE id=?", (id,))
    conn.commit()

    # 입력 상자 초기화
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    manufacturer_entry.delete(0, tk.END)
    model_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    # 제품 목록 표시
    show_products()

# 제품 목록 표시 함수
def show_products():
    # 기존에 표시된 목록 삭제
    product_list.delete(0, tk.END)

    # 데이터베이스에서 모든 제품 가져오기
    c.execute("SELECT * FROM robot_products")
    rows = c.fetchall()

    # 제품 목록에 추가
    for row in rows:
        product_list.insert(tk.END, f"{row[1]} ({row[2]}, {row[3]}) - {row[4]} 원")

# 추가, 수정, 삭제 버튼 생성
add_button = tk.Button(mac, text="추가", command=add_product)
add_button.grid(row=4, column=0)

update_button = tk.Button(mac, text="수정", command=update_product)
update_button.grid(row=4, column=1)

delete_button = tk.Button(mac, text="삭제", command=delete_product)
delete_button.grid(row=4, column=2)

# 제품 목록 표시
product_list = tk.Listbox(mac, height=10, width=70)
product_list.grid(row=5, columnspan=3)

# 제품 선택 시 상세 정보 표시
def show_product(event):
    index = product_list.curselection()[0]
    product_id = product_list.get(index).split('.')[0]
    c.execute("SELECT * FROM robot_products WHERE id=?", (product_id,))
    row = c.fetchone()
    id_entry.delete(0, tk.END)
    id_entry.insert(tk.END, row[0])
    name_entry.delete(0, tk.END)
    name_entry.insert(tk.END, row[1])
    manufacturer_entry.delete(0, tk.END)
    manufacturer_entry.insert(tk.END, row[2])
    model_entry.delete(0, tk.END)
    model_entry.insert(tk.END, row[3])
    price_entry.delete(0, tk.END)
    price_entry.insert(tk.END, row[4])

product_list.bind('<<ListboxSelect>>', show_product)

# 제품 ID 입력 상자
tk.Label(mac, text="제품 ID").grid(row=6)
id_entry = tk.Entry(mac)
id_entry.grid(row=6, column=1)

# 제품 목록 표시 버튼 생성
show_products_button = tk.Button(mac, text="제품 목록 표시", command=show_products)
show_products_button.grid(row=7, column=0, columnspan=3)

if __name__ == '__main__':
    mac.mainloop()

# 데이터베이스 연결 종료
conn.close()
