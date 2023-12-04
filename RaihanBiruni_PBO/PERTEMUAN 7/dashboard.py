import tkinter as tk
from tkinter import Menu, Label
from kubus import Kubus_frame
from balok import BalokFrame
from bola import BolaFrame

def destroy_window(window):
    window.destroy()

def new_window(_class):
        new = tk.Toplevel(root)
        new.title(_class.__name__)
        _class(new)

# root window app
root = tk.Tk()
root.title('Menu Demo')
root.geometry("900x400")

# membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)

# membuar menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)

# menambah menu item
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

data_menu.add_command(
    label='Kubus', command=lambda: new_window(Kubus_frame)
)
data_menu.add_command(
    label='Balok', command=lambda: new_window(BalokFrame)
)
data_menu.add_command(
    label='Bola', command=lambda: new_window(BolaFrame)
)

# mamasukan menu ke menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=data_menu
)

root.mainloop()
