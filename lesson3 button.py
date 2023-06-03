def add_label():
    label = tk.Label(win,text='new')
    label.pack()
def say_hello():
    print('hello')
def counter():
    global count
    count +=1
    btn4['text'] = f'Счетчик: {count}'
import tkinter as tk

win = tk.Tk()
win.title('Graph')
win.geometry(f'400x500+100+200')
count = 0
btn = tk.Button(win,text='Hello',
                command=say_hello,

                )
btn2 = tk.Button(win,text='Add new label',
                command=add_label,
                )
btn3 = tk.Button(win,text='Add new label lambda',
                command=lambda:tk.Label(win,text='new lambda').pack()
                )
btn4 = tk.Button(win,text= f'Счетчик: {count}',
                command=counter,
                 bg='red',
                 activebackground='blue',
                 state=tk.NORMAL
                )
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
win.mainloop()
