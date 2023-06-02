import tkinter as tk

win = tk.Tk()
win.title('Graph')
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False,photo)
win.config(bg='blue')
win.geometry('500x600+100+200')
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(False, False)

win.mainloop()
