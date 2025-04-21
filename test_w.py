import tkinter as tk
from tkinter import ttk


class MiVentana(tk.Tk):
    def __init__(self):
        super(MiVentana, self).__init__()
        self._configMiVentana()

    def _configMiVentana(self):
        self.geometry('250x350')
        self.config(bg='#100520')
        self.bind('<Configure>', self.getSize)

        bt = ttk.Button(self, text='cerrar', command=self.destroy)
        bt.pack(expand=True)
        

    def getSize(self, e=tk.Event) -> None:
        w, h = self.winfo_width(), self.winfo_height()
        self.title(f'{w}x{h}')


if __name__ == '__main__':
    vn = MiVentana()
    vn.mainloop()