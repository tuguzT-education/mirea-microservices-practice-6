from tkinter import *
from tkinter.ttk import *


def clicked():
    message = "Text: " + txt.get()
    Ibl.configure(text=message)


window = Tk()
combo = Combobox(window)
window.title("123")
window.geometry('500x200')
Ibl = Label(window, text="Hello, world!", font=("Arial Bold", 50))
Ibl.grid(column=0, row=0)
btn = Button(window, text="OK", command=clicked)
btn.grid(column=0, row=1)
txt = Entry(window, width=10)
txt.grid(column=1, row=1)
combo['values'] = (1, 2, 3, 4, 5)
combo.current(1)  # set the selected item
combo.grid(column=0, row=2)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=1, row=2)

rad1 = Radiobutton(window, text='1-st', value=1)
rad2 = Radiobutton(window, text='2-nd', value=2)
rad3 = Radiobutton(window, text='3-rd', value=3)
rad1.grid(column=0, row=3)
rad2.grid(column=0, row=4)
rad3.grid(column=0, row=5)

window.mainloop()
