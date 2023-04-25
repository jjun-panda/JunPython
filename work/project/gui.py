from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jjun/figma_python/python/build/assets/frame0")




window = Tk()

window.geometry("800x800+100+100")
window.configure(bg = "#E9E9E9")


canvas = Canvas(
    window,
    bg = "#E9E9E9",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    543.0,
    216.0,
    768.0,
    441.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    32.0,
    471.0,
    257.0,
    696.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    288.0,
    216.0,
    513.0,
    441.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    287.0,
    471.0,
    512.0,
    696.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    32.0,
    216.0,
    257.0,
    441.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    544.0,
    386.0,
    anchor="nw",
    text="계산기",
    fill="#000000",
    font=("NotoSansKR Regular", 32 * -1)
)

canvas.create_text(
    33.0,
    386.0,
    anchor="nw",
    text="알람",
    fill="#000000",
    font=("NotoSansKR Regular", 32 * -1)
)

canvas.create_text(
    33.0,
    641.0,
    anchor="nw",
    text="주소록",
    fill="#000000",
    font=("NotoSansKR Regular", 32 * -1)
)

canvas.create_text(
    288.0,
    386.0,
    anchor="nw",
    text="미니게임",
    fill="#000000",
    font=("NotoSansKR Regular", 32 * -1)
)

canvas.create_text(
    288.0,
    641.0,
    anchor="nw",
    text="관리시스템",
    fill="#000000",
    font=("NotoSansKR Regular", 32 * -1)
)

canvas.create_text(
    54.0,
    28.0,
    anchor="nw",
    text="9:41",
    fill="#1E1E1E",
    font=("SFProText Semibold", 34 * -1)
)
window.resizable(False, False)
window.mainloop()
