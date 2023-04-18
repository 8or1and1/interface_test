from tkinter import *
from tkinter import ttk


def finish():
    root.destroy()
    print('App is closed')

root = Tk()
root.title("Database migration tool")
root.geometry("800x800+2500+100")
root.resizable(False, False)
root.iconbitmap(default='favicon.ico')

root.protocol('WM_DELETE_WINDOW', finish)

btn = ttk.Button(text="Click")
btn.pack()

root.mainloop()