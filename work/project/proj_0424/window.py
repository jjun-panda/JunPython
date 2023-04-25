import subprocess
import tkinter as tk
# import jjun_news as mac

def run_external_file():
    subprocess.call(['python', './jjun_news.py'])

app = tk.Tk()
buttonExample = tk.Button(app, 
            text="Create new window",
            command=run_external_file)
buttonExample.pack()

app.mainloop()