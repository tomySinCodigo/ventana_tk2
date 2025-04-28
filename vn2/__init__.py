import tkinter as tk
from tkinter import ttk
import funciones as fun
from main import KBarra


class Ventana(tk.Tk):
    def __init__(self):
        super(Ventana, self).__init__()
        self._configVentana()

    def _configVentana(self):
        self.bind('<Configure>', self.getSize)
        # bt = ttk.Button(self, text='cerrar', command=self.destroy)
        # bt.pack(expand=True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.bar = KBarra(self)
        self.bar.grid(row=0, column=0, sticky='wens')


        self.reloadConfigs()

    def getSize(self, e=tk.Event) -> None:
        w, h = self.winfo_width(), self.winfo_height()
        self.title(f'{w}x{h}')

    def reloadConfigs(self):
        """reload configs toml"""
        vc = fun.getConfig('ventana')
        w, h = vc.get('size')
        bg = vc.get('bg')
        self.geometry(f'{w}x{h}')
        self.config(bg=bg)

        dbar = fun.getConfig('bar')
        barbg = dbar.get('bg')
        self.bar.setBg(**barbg)



if __name__ == '__main__':
    vn = Ventana()
    vn.mainloop()