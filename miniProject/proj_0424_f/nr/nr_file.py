import datetime
import winsound
from threading import Thread
from tkinter import Tk, PanedWindow, StringVar, ttk, Toplevel
from tkinter.ttk import Label, Button, Treeview
import time
from alarm_image import img_win
from alarm_dao import *

# 새로 열리는 창(Tk())이 스크린의 중간에 열리도록 하는 코드
def center_win(win, width, height) :
    # 스크린의 가로, 세로 크기를 구한다.
    screen_w = win.winfo_screenwidth() # 현재 실행된 컴퓨터의 해상도 중 가로 길이를 return
    screen_h = win.winfo_screenheight() # 현재 실행된 컴퓨터의 해상도 중 세로 길이를 return

    # 새로 열리는 창을 스크린의 중앙으로 이동시키기 위한 좌표 계산
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)

    # 새로 열리는 창의 위치를 설정
    win.geometry(f"{width}x{height}+{x}+{y}")

# 시간 구현에 대한 함수
def times() :
    current_time = time.strftime("%I : %M : %S %p")
    clock.config(text=current_time)
    clock.after(200, times)

# 알람 설정 버튼 클릭 시 이벤트
def set_btnEvtHandler() :
    # 알람 설정 창 생성
    new_win = Toplevel()
    new_win.title('Set Alarm')
    new_win.geometry("340x230+900+230")

    # 설정 버튼 클릭 시 이벤트
    def set_btn_btnEvtHandler():
        global no

        # 선택한 알람 시간을 데이터 베이스에 넣는 함수
        insert_data((hour_choose.get(), min_choose.get(), ap_choose.get()))
        # treeview에 선택한 알람 시간을 넣는 것
        tree.insert('', 'end', values=(no, hour_choose.get(), min_choose.get(), ap_choose.get()))
        no += 1

        # 알람이 울리는 것을 다른 스레드에서 실행, 알람 설정 버튼을 누름과 동시에 창이 꺼짐
        timer = Thread(target=alram)
        timer.start()
        new_win.destroy()

    # 설정한 시간과 현재 시간이 같으면 새로운 창을 띄워 쉬는 시간인 것을 알리고, 음악을 재생
    def alram():
        set_alarm = f"{hour.get()}:{minute.get()} {ap.get()}"

        while True:
            # 1초마다 갱신
            time.sleep(1)

            # 현재 시간과 설정한 시간을 같을 때, 창 생성, 노래 재생
            c_time = datetime.datetime.now().strftime("%I:%M %p")
            if c_time == set_alarm:
                winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
                img_win()
                return

    # 알람 설정 창에 대한 GUI
    set_a_lbl = Label(new_win, text="알람 설정", font=("UhBee Se_hyun", 20))
    set_a_lbl.grid(row=0, column=2, columnspan=2, pady=15, padx=13)

    detail_h_lbl = Label(new_win, text="시", font=("UhBee Se_hyun", 12))
    detail_h_lbl.grid(row=1, column=2)

    detail_m_lbl = Label(new_win, text="분", font=("UhBee Se_hyun", 12))
    detail_m_lbl.grid(row=1, column=4)

    detail_a_lbl = Label(new_win, text="AM/PM", font=("UhBee Se_hyun", 10))
    detail_a_lbl.grid(row=1, column=5)

    # 시 콤보박스
    hour = StringVar(new_win)
    hour_choose = ttk.Combobox(new_win, textvariable=hour, width=10)

    hour_choose['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
    hour_choose.grid(row=2, column=2)
    hour_choose.current()

    set_lbl = Label(new_win, text=":")
    set_lbl.grid(row=2, column=3)

    # 분 콤보박스
    minute = StringVar(new_win)
    min_choose = ttk.Combobox(new_win, textvariable=minute, width=10)

    min_choose['values'] = (
        '00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59'
    )
    min_choose.grid(row=2, column=4)

    # am/pm 콤보박스
    ap = StringVar(new_win)
    ap_choose = ttk.Combobox(new_win, textvariable=ap, width=5)

    ap_choose['values'] = ('AM', 'PM')
    ap_choose.grid(row=2, column=5)

    btn_create = Button(new_win, text="설정", command=set_btn_btnEvtHandler)
    btn_create.grid(row=3, column=2, columnspan=6, pady=40, padx=125)

    # 콤보박스의 초기 기본 값
    hour_choose.current(0)
    min_choose.current(0)
    ap_choose.current(0)

    new_win.mainloop()

# 알람을 삭제하는 함수
def alarm_delete() :
    # 트리뷰에서 항목 선택
    selected_item = tree.focus()

    # 선택한 항목의 번호
    item_details = tree.item(selected_item)['values'][0]

    # 트리뷰에서 항목 삭제
    tree.delete(selected_item)
    # 데이터베이스에서 항목 삭제
    delete(item_details)

# sql table 생성
create_table()

# 객체 생성
win = Tk()
win.title('Alarm Clock')
# 새로 열리는 창의 크기 설정
width, height = 340, 480
# 새로 열리는 창을 중앙으로 이동
center_win(win, width, height)

# title 생성
title = Label(win, text=" 알람 시계 ", font=("UhBee Se_hyun", 25), background="#B8F0F0")
title.grid(row=1)

# 현재 시간을 알리는 시계 생성
clock = Label(win, font=("UhBee Se_hyun", 30))
clock.grid(row=2, pady=25)
times()

# 알람 시계 목록을 나타내는 Listbox의 title
list_label = Label(win, text="알람 시계 목록", font=("UhBee Se_hyun", 12))
list_label.grid(row=3)

# 알람 시계 목록을 나타내는 Listbox
# alram_list_box = Listbox(win, width=47)
# alram_list_box.grid(row=4, pady=20)

alarm_list = ["no", "hour", "minute", "ap"]
# data_list = [
#     (1, '04', '25', 'AM'),
#     (2, '07', '25', 'PM'),
#     (3, '09', '25', 'PM'),
#     (4, '11', '25', 'AM')
# ]
data_list = []
no = 1
# 알람 시계 목록을 나타내는 Treeview
tree = Treeview(win, columns=alarm_list, show="headings")
tree["columns"] = ("no", "hour", "minute", "ap")

tree.grid(row=4)

for i, col in enumerate(alarm_list) :
    tree.heading(col, text=col.title())
for i, item in enumerate(data_list) :
    tree.insert('', 'end', iid='IID%d' %(i), values=item)

tree.column("no", width=83)
tree.column("hour", width=83)
tree.column("minute", width=83)
tree.column("ap", width=83)

tree.heading("no", text="no")
tree.heading("hour", text="시")
tree.heading("minute", text="분")
tree.heading("ap", text="AM/PM")

# 버튼을 x축으로 나란히 놓기 위해 지정
panewindow = PanedWindow(relief="raised", bd=0)
panewindow.grid(row=5, padx=5, pady=5)

# 버튼 생성
button1 = Button(panewindow, text="알람 설정", width=22, command=set_btnEvtHandler)
button2 = Button(panewindow, text="알람 삭제", width=22, command=alarm_delete)

panewindow.add(button1)
panewindow.add(button2)

if __name__ == '__main__':
    win.mainloop()