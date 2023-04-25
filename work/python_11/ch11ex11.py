from tkinter import Tk, Button, Entry, END

opers = []
nums = []
numStr = ''

def calc(target) :
    ch = target['text']
    global opers, nums, numStr
    if len(ch) == 1 :
        if ch != 'C' and ch != '%' and ch != 'v': txt_result.insert(END, ch)
        if ord(ch) >= 48 and ord(ch) <= 57 :
            numStr += ch;
        if ch=='+' or ch=='-' or ch=='*' or ch=='/' :
            nums.append(numStr)
            opers.append(ch)
            numStr = '';
        if ch == '=' :
            nums.append(numStr)
            # print(nums)
            # print(opers)
            result = int(nums[0]);
            for i, oper in enumerate(opers) :
                if oper == '+' :
                    result += int(nums[i+1])
                elif oper == '-' :
                    result -= int(nums[i + 1])
                elif oper == '*' :
                    result *= int(nums[i + 1])
                elif oper == '/' :
                    result //= int(nums[i + 1])

            txt_result.insert(END, str(result))

mac = Tk()

txt_result = Entry(mac, justify="right")
txt_result.grid(row=0, column=0, columnspan=5, pady=2)

btns = [
    [Button(mac, text="MC"),Button(mac, text="MR"),Button(mac, text="MS"),Button(mac, text="M+"),Button(mac, text="M-")],
    [Button(mac, text="<-"),Button(mac, text="CE"),Button(mac, text="C"),Button(mac, text="+-"),Button(mac, text="v")],
    [Button(mac, text="7"),Button(mac, text="8"),Button(mac, text="9"),Button(mac, text="/"),Button(mac, text="%")],
    [Button(mac, text="4"),Button(mac, text="5"),Button(mac, text="6"),Button(mac, text="*"),Button(mac, text="1/x")],
    [Button(mac, text="1"),Button(mac, text="2"),Button(mac, text="3"),Button(mac, text="-"),Button(mac, text="=")],
    [Button(mac, text="0"),Button(mac, text="."),Button(mac, text="+")]
]

for btnArr in btns :
    for btn in btnArr :
        def clickEvent(target = btn):
            calc(target)
        btn.config(command=clickEvent)
        
for i in range(1,6) :
    for j in range(5) :
        if i == 6 and j == 3:
            break
        if i == 5 and j == 4 :
            btns[i - 1][j].grid(row=i, column=j, rowspan=2, sticky='wens', padx=2, pady=2)
        else :
            btns[i - 1][j].grid(row=i, column=j, padx=2, pady=2, sticky='wens')

btns[5][0].grid(row=6, column=0, columnspan=2, sticky='wens', padx=2, pady=2)
btns[5][1].grid(row=6, column=2, padx=2, pady=2, sticky='wens')
btns[5][2].grid(row=6, column=3, padx=2, pady=2, sticky='wens')

if __name__ == "__main__":
    mac.mainloop()