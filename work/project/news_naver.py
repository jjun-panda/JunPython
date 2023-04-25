import tkinter as tk
from tkinter import ttk
from SearchList import getSearchList
import time
import webbrowser

def update_label(url, label):
    search_list = getSearchList(url, "div.sc-fQvxkG.hovjdV")
    div_list = search_list[0].find_all('li', class_='sc-fHCHyC jhKFuK')
    news_list = [element.find('a') for element in div_list]
    for i, news in enumerate(news_list):
        btn = tk.Button(frame, text=news.text.strip(), font=('Arial', 12), anchor='w', justify='left', command=lambda url=news['href']: webbrowser.open(url))
        btn.pack(fill=tk.X, pady=5, padx=5)
    label.config(text="Last updated: " + time.strftime("%Y-%m-%d %H:%M:%S"))

def update_yahoo_jp_label():
    update_label("https://news.yahoo.co.jp/", yahoo_jp_last_update)

root = tk.Tk()
root.title("News Headline")
root.geometry("800x800")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

yahoo_jp_news_btn = tk.Button(root, text="Yahoo_jp News", font=('Arial', 12), command=update_yahoo_jp_label)
yahoo_jp_news_btn.pack(side=tk.TOP, pady=5)

yahoo_jp_last_update = tk.Label(root, text="Last updated: ", font=('Arial', 10))
yahoo_jp_last_update.pack(side=tk.BOTTOM, pady=5)

update_yahoo_jp_label()

if __name__ == '__main__':
    root.mainloop()
