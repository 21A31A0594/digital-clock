from tkinter import*
from tkinter.ttk import*
from time import strftime
root = Tk()
root.title('CLOCK')
def time():
    display=strftime('%H:%M:%S %p')
    lbl.config(text=display)
    lbl.after(1000,time)
lbl=Label(root,font=('verdana',50,'bold'), background='navyblue',foreground='white' )
lbl.pack(anchor='center')
time()
mainloop()