import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class BalokFrame:
    def __init__(self, root):
        self.root = root
        root.title("KALKULATOR LUAS DAN VOLUME BALOK")
        frame = Frame(root)
        frame.pack(padx=40, pady=40)

        nama = Label(frame, text="Raihan Biruni")
        nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        panjang_label = Label(frame, text="Panjang:")
        panjang_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        lebar_label = Label(frame, text="Lebar:")
        lebar_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        tinggi_label = Label(frame, text="Tinggi:")
        tinggi_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.txtpanjang = Entry(frame)
        self.txtpanjang.grid(row=1, column=1)

        self.txtlebar = Entry(frame)
        self.txtlebar.grid(row=2, column=1)

        self.txttinggi = Entry(frame)
        self.txttinggi.grid(row=3, column=1)

        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        luas_label = Label(frame, text="Luas:")
        luas_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        volume_label = Label(frame, text="Volume:")
        volume_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(frame)
        self.txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggi = float(self.txttinggi.get())

        L = round(((2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)), 2)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggi = float(self.txttinggi.get())

        V = round((panjang*lebar*tinggi), 2)

        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == "__main__":
    app = tk.Tk()
    kalkulator = BalokFrame(app)
    app.mainloop()
