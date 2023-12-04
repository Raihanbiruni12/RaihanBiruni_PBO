import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class Kubus_frame:
    def __init__(self, master):
        super().__init__(master, bd=50)
        label = Label(self, text= "Halaman Kubus"())
        label.grid(row=0, column=0,columnspan=2, sticky='n', pady=30)
        
    def __init__(self, root):
        self.root = root
        root.title("KALKULATOR LUAS DAN VOLUME KUBUS")
        frame = Frame(root)
        frame.pack(padx=40, pady=40)

        nama = Label(frame, text="Raihan Biruni")
        nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.sisi_label = Label(frame, text="Sisi:")
        self.sisi_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txtsisi = Entry(frame)
        self.txtsisi.grid(row=1, column=1)

        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        luas = Label(frame, text="Luas:")
        luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        volume = Label(frame, text="Volume:")
        volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(frame)
        self.txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        s = float(self.txtsisi.get())
        L = round((6 * s**2), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        s = float(self.txtsisi.get())
        V = round((s**3), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == "__main__":
    app = tk.Tk()
    kalkulator = Kubus_frame(app)
    app.mainloop()
