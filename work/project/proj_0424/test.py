import subprocess
import tkinter as tk

def run_nr_file():
    subprocess.call(['python', './nr/nr_file.py'])

def run_js_file():
    subprocess.call(['python', './js/js_file.py'])

def run_sh_file():
    subprocess.call(['python', './sh/sh_file.py'])

def run_mc_file():
    subprocess.call(['python', './mc/mc_file.py'])

def run_mg_file():
    subprocess.call(['python', './mg/mg_file.py'])

# 윈도우 생성
mac = tk.Tk()
mac.title("홈 화면")
mac.geometry("800x800")

# 배경 이미지 설정
bg_img = tk.PhotoImage(file="bgbg.png", master=mac)
bg_label = tk.Label(mac, image=bg_img)
bg_label.place(x=0, y=0)

# 앱 아이콘 생성
icon1 = tk.PhotoImage(file="ico_menu1.png", master=mac)
icon1_label = tk.Button(mac, width=225, height=225, image=icon1, command=run_nr_file, cursor="hand2", bg="#B8DFD9")
icon1_label.place(x=32, y=200)

icon2 = tk.PhotoImage(file="ico_menu2.png", master=mac)
icon2_label = tk.Button(mac, width=225, height=225, image=icon2, command=run_mc_file, cursor="hand2", bg="#B8DFD9")
icon2_label.place(x=288, y=200)

icon3 = tk.PhotoImage(file="ico_menu3.png", master=mac)
icon3_label = tk.Button(mac, width=225, height=225, image=icon3, command=run_mg_file, cursor="hand2", bg="#B8DFD9")
icon3_label.place(x=543, y=200)

icon4 = tk.PhotoImage(file="ico_menu4.png", master=mac)
icon4_label = tk.Button(mac, width=225, height=225, image=icon4, command=run_sh_file, cursor="hand2", bg="#B8DFD9")
icon4_label.place(x=32, y=460)

icon5 = tk.PhotoImage(file="ico_menu5.png", master=mac)
icon5_label = tk.Button(mac, width=225, height=225, image=icon5, command=run_js_file, cursor="hand2", bg="#B8DFD9")
icon5_label.place(x=288, y=460)

# 앱 이름 생성
app1 = tk.Label(mac, text="시끄러! 알람", font=("Pretendard", 28))
app1.place(x=33, y=380)

app2 = tk.Label(mac, text="계산기", font=("Pretendard", 28))
app2.place(x=288, y=380)

app3 = tk.Label(mac, text="모기잡아라", font=("Pretendard", 28))
app3.place(x=544, y=380)

app4 = tk.Label(mac, text="주소록", font=("Pretendard", 28))
app4.place(x=33, y=637)

app5 = tk.Label(mac, text="실시간뉴스", font=("Pretendard", 28))
app5.place(x=288, y=637)

# 윈도우 실행
mac.mainloop()
