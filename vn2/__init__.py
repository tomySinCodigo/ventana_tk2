import tkinter as tk
from tkinter import ttk
import funciones as fun
from main import KBarra, KGrip
from mytray import MyTray
from position import Position


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
        self.tray = MyTray(self, image_icon="image10.png")
        self.tray.run()
        self.bar.basicbuttons.bt_close.config(command=self.tray.closeWindow)
        self.bar.basicbuttons.bt_min.config(command=self.tray.minimizeWindow)
        self.bar.basicbuttons.bt_mm.config(command=self.restoreWindow)
        self.bar.basicbuttons.bt_pin.config(command=self.onTop)

        self.overrideredirect(True)
        self.TOP = True
        self.bar.basicbuttons.bt_pin.setActive(self.TOP)
        self.onTop()

        self.CX, self.CY = 0, 0
        self.bind('<ButtonPress-3>', self._startMove)
        self.bind('<ButtonRelease-3>', self._stopMove)
        self.bind('<B3-Motion>', self._onMotion)

        self.pos = Position(self)
        self.bar.basicbuttons.bt_lr.config(command=self.pos.toggle)
        self.addGrip()

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

        title_cnf = dbar.get('title')
        self.setTitle(title_cnf.get('text'))

        n1, n2 = vc.get('proportion')
        self.pos.sz = n1/n2
        self.pos.modx = vc.get('modx')
        self.pos.mody = vc.get('mody')
        self.pos.modw = vc.get('modw')
        self.pos.modh = vc.get('modh')
        self.grip.config(bg=bg)

    def setTitle(self, title:str) -> None:
        """set title of window"""
        self.bar.setTitle(title)
        self.tray.setTitle(title)

    def restoreWindow(self):
        """restore window"""
        std = "normal" if self.state() == "zoomed" else "zoomed"
        self.wm_state(std)

    def onTop(self):
        """set window on top"""
        n = 1 if self.TOP else 0
        self.wm_attributes("-topmost", n)
        self.TOP = not self.TOP

    def _startMove(self, event):
        self.CX, self.CY = event.x, event.y

    def _stopMove(self, event):
        self.CX, self.CY = 0, 0

    def _onMotion(self, event):
        x = self.winfo_x() + (event.x - self.CX)
        y = self.winfo_y() + (event.y - self.CY)
        self.geometry(f"+{x}+{y}")

    def addGrip(self):
        self.grip = KGrip(self)
        self.grip.place(relx=0.996, rely=0.994, anchor='se')
        self.grip.bind('<Button-1>', self.grip.startResize)
        # self.grip.bind('<B1-Motion>', self.grip.performResize)
        self.grip.bind('<ButtonRelease-1>', self.grip.performResize)


if __name__ == '__main__':
    vn = Ventana()
    vn.mainloop()