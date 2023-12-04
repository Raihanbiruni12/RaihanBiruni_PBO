import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

class BolaFrame:
    def __init__(self, root):
        self.root = root
        root.title("KALKULATOR LUAS DAN VOLUME BOLA")
        frame = Frame(root)
        frame.pack(padx=40, pady=40)

        nama = Label(frame, text="Raihan Biruni")
        nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        jari_jari_label = Label(frame, text="Jari-Jari:")
        jari_jari_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(frame)
        self.txtJariJari.grid(row=1, column=1)

        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        luas_label = Label(frame, text="Luas:")
        luas_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        volume_label = Label(frame, text="Volume:")
        volume_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(frame)
        self.txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        r = float(self.txtJariJari.get())
        L = round((4 * pi * r**2), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        r = float(self.txtJariJari.get())
        V = round((4/3 * pi * r**3), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == "__main__":
    app = tk.Tk()
    kalkulator = BolaFrame(app)
    app.mainloop()
