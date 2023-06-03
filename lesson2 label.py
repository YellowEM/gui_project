import tkinter as tk

win = tk.Tk()
win.title('Graph')
win.geometry(f'500x600+100+200')

label_1 = tk.Label(win, text='''Hello!
world!''',
                   bg='red',
                   fg='white',
                   font=('Arial', 15, 'bold'),
                   padx=10,
                   pady=40,
                   width=20,
                   heigh=10,
                   anchor='w',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )

label_1.pack()

win.mainloop()
