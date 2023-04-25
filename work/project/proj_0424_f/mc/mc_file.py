from tkinter import *
import tkinter.messagebox as msgbox

IVORY = "#FFFFF0"
PINK = "#FFC0CB"
SKYBLUE = "#87CEEB"
GREEN = "#90EE90"

def clicked(blist) : #"←" 버튼 클릭 시 뒤에 하나씩 지워지는 함수
    if blist == "←":
        text_entry.delete(len(text_entry.get())-1) # ←클릭 시 하나 지우기
    else :
        text_entry.insert(END, blist) # 마지막에 추가하

def click_del(): # "Reset" 버튼 클릭 시 전체 지워지는 함수
    text_entry.delete(0, END) # 지울 번호 0번 index부터 마지막index까지
    lbl.config(text="")

def calculate(event=None): # "=" 버튼 클릭 시 계산 결과 값 나오게 하는 함수
    try :# 예외처리 정상
        result = eval(text_entry.get())  # Entry에 값을 가지고와서 계산 해준다
        # eval()은 파이썬에서 수식을 간단하게 계산해주는 함수이다
    except:# 예외처리 비정상
        lbl.config(text="계산식 오류 입니다")
    else:
        lbl.config(text=result)

def check_input(event=None) :
    input_str = text_entry.get()
    if any(char.isalpha() for char in input_str):
        msgbox.showerror("Error", "문자가 입력되었습니다 숫자만 입력하세요")


win = Tk() # tkinter 창 나옴
win.title("계산기") # 제목
win.resizable(False, False) # tkinter 창 크기 조절
win.geometry("500x350")
win.config(padx=2, pady=2, bg=IVORY)

blists = [# 계산기에 들어가는 숫자 버튼
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['←', '0', '.', '+']
]

text_entry = Entry(win, width=30, font=("Pretendard", 20), bg=IVORY, justify="right") # 숫자 입력 박스 높이는 30, font 지정, 오른쪽 정렬
text_entry.grid(column=0, row=0, columnspan=4)
text_entry.focus() # 포커스 클릭 하지 않아도 보이게 함

text_entry.bind("<Return>", calculate)
text_entry.bind("<KeyRelease>", check_input)

lbl = Label(win, text="계산할 숫자를 입력하세요", width=20, font=("Pretendard", 30), bg=IVORY) # 결과값 출력되는 곳
lbl.grid(column=0, row=1, columnspan=4, pady=15)

for r in range(4):
    for c in range(4):
        blist = blists[r][c]
        button = Button(win, text=blist, width=8, font=("Pretendard", 15), bg=SKYBLUE, command=lambda x=blist : clicked(x)) # 계산기 안에 버튼 클릭 시 입력
        button.grid(row=r+2, column=c, pady=2)

cle_btn = Button(win, text="Reset", width=16, font=("Pretendard", 17, "bold"), bg=GREEN, command=click_del) # 초기화 버튼 높이 지정, 색상 지정
cle_btn.grid(column=0, row=6, columnspan=2, pady=5)

cal_btn = Button(win, text="=", width=16, font=("Pretendard", 17, "bold"), bg=GREEN, command=calculate) # "=" 결과 버튼 높이 지정, 색상 지정
cal_btn.grid(column=2, row=6, columnspan=2, pady=5)

if __name__ == '__main__':
    win.mainloop()