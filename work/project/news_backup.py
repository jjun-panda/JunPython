import tkinter as tk
from tkinter import PhotoImage, ttk
from SearchList import getSearchList
import time
import webbrowser

def clear_list():
    for button in frame.winfo_children():
        button.destroy()

def update_label(url, label, update_time):
    clear_list()
    if "daum_1" in url:
        search_list = getSearchList(url, "div.box_etc")
        seb_list = search_list[0].find_all('strong', class_='tit_thumb')
        news_list = [element.find("a") for element in seb_list]
    elif "daum_2" in url:
        search_list = getSearchList(url, "div.box_etc")
        seb_list = search_list[0].find_all('strong', class_='tit_thumb')
        news_list = [element.find("a") for element in seb_list]
    elif "daum_3" in url:
        search_list = getSearchList(url, "div.box_etc")
        seb_list = search_list[0].find_all('strong', class_='tit_thumb')
        news_list = [element.find("a") for element in seb_list]
    elif "daum_4" in url:
        search_list = getSearchList(url, "div.box_etc")
        seb_list = search_list[0].find_all('strong', class_='tit_thumb')
        news_list = [element.find("a") for element in seb_list]
    else:
        return
    
    for child in label.winfo_children():
        child.destroy()

    for i, news in enumerate(news_list):
        btn = tk.Button(frame, text=news.text.strip(), font=("Pretendard", 24), width=35, anchor="w", justify="left", command=lambda url=news["href"]: webbrowser.open(url), cursor="hand2")
        btn.pack(fill=tk.X, pady=5, padx=5)
    
    # 클릭한 시간(업데이트한 시간)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    label.config(text=f"Last updated: {current_time}")
    update_time.config(text=f"Last updated: {current_time}")

def update_yahoo_jp_label():
    update_label("https://news.daum.net/breakingnews/society", yahoo_jp_last_update, yahoo_jp_last_update)

def update_daum_label():
    update_label("https://news.daum.net/breakingnews/politics", daum_last_update, daum_last_update)

def update_yonhap_label():
    update_label("https://news.daum.net/breakingnews/economic", yonhap_last_update, yonhap_last_update)

def update_hani_label():
    update_label("https://news.daum.net/breakingnews/foreign", hani_last_update, hani_last_update)

def update_all():
    update_yahoo_jp_label()
    update_daum_label()
    update_yonhap_label()
    update_hani_label()

mac = tk.Tk()
mac.title("News Live")
mac.geometry("800x800")

canvas = tk.Canvas(mac, width=500, height=500)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(mac, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# 야휴재팬뉴스
yahoo_img = PhotoImage(file="yahoo.png", master=mac, width=20, height=20)
yahoo_jp_news_btn = tk.Button(mac, text="  다음뉴스(사회)", font=("Pretendard", 12), command=update_yahoo_jp_label, compound="left", image = yahoo_img, width=120, height=40, cursor="hand2")
yahoo_jp_news_btn.pack(pady=5)
yahoo_jp_last_update = tk.Label(mac, text="Last updated: ", font=("Pretendard", 10))
yahoo_jp_last_update.pack()

# 다음뉴스
daum_img = PhotoImage(file="daum.png", master=mac, width=20, height=20)
daum_news_btn = tk.Button(mac, text="  다음뉴스", font=("Pretendard", 12), command=update_daum_label,compound="left", image = daum_img, width=120, height=40, cursor="hand2")
daum_news_btn.pack(pady=5, padx=20)
daum_last_update = tk.Label(mac, text="Last updated: ", font=("Pretendard", 10))
daum_last_update.pack()

# 연합뉴스
yonhap_img = PhotoImage(file="yonhap.png", master=mac, width=20, height=20)
yonhap_news_btn = tk.Button(mac, text="  연합뉴스", font=("Pretendard", 12), command=update_yonhap_label, compound="left", image = yonhap_img, width=120, height=40, cursor="hand2")
yonhap_news_btn.pack(pady=5)
yonhap_last_update = tk.Label(mac, text="Last updated: ", font=("Pretendard", 10))
yonhap_last_update.pack()

# 한겨레 뉴스
hani_img = PhotoImage(file="hani.png", master=mac, width=20, height=20)
hani_news_btn = tk.Button(mac, text="  한겨레뉴스", font=("Pretendard", 12), command=update_hani_label, compound="left", image = hani_img, width=120, height=40, cursor="hand2")
hani_news_btn.pack(pady=5)
hani_last_update = tk.Label(mac, text="Last updated: ", font=("Pretendard", 10))
hani_last_update.pack()

# 전체 업데이트
all_img = PhotoImage(file="re.png", master=mac, width=20, height=20)
all_update_btn = tk.Button(mac, text="  All UPDATE", font=("Pretendard", 12), command=update_all, compound="left", image = all_img, width=120, height=40, cursor="hand2")
all_update_btn.pack(pady=5, side="bottom")


update_daum_label()
update_yonhap_label()
update_hani_label()
update_yahoo_jp_label()


if __name__ == "__main__":
    mac.mainloop()

