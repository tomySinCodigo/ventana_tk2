import ctypes


class Position():
    """set position window - left, right, toggle, full"""
    def __init__(self, window):
        self.window = window
        self._configPosition()

    def _configPosition(self):
        self.bar = 30
        self.modx = 0
        self.mody = 0
        self.modw = 0
        self.modh = 0
        self.sz = 1/3
        self._LEFT = False
        
    def getSizeScreen(self) -> tuple[int, int]:
        """Get size of screen"""
        rs = ctypes.windll.user32
        rs.SetProcessDPIAware()
        return rs.GetSystemMetrics(0), rs.GetSystemMetrics(1)
    
    def move(self, left=True) -> None:
        """Move window"""
        wp, hp = self.getSizeScreen()
        if self.bar != 0:
            hp -= self.bar
        if left:
            x, y = 0 + self.modx, 0 + self.mody
            w, h = (wp * self.sz) + self.modw, hp + self.modh
        else:
            width = wp * self.sz
            x, y = (wp - width) + self.modx, 0 + self.mody
            w, h = width + self.modw, hp + self.modh
        w, h, x, y = int(w), int(h), int(x), int(y)
        self.window.geometry(f'{w}x{h}+{x}+{y}')
        self._LEFT = left

    def full(self):
        wp, hp = self.getSizeScreen()
        if self.bar != 0:
            hp += self.bar
        x, y = 0 + self.modx, 0 + self.mody
        self.window.geometry(f'{wp}x{hp+30}+{x}+{y}')

    def left(self):
        self.move(left=True)

    def right(self):
        self.move(left=False)

    def toggle(self):
        self.right() if self._LEFT else self.left()


if __name__ == '__main__':
    import tkinter as tk
    from tkinter import ttk
    
    
    class VentanaTest(tk.Tk):
        def __init__(self):
            super(VentanaTest, self).__init__()
            self._configVentanaTest()
    
        def _configVentanaTest(self):
            self.geometry('250x350')
            self.config(bg='#100520')
            self.bind('<Configure>', self.getSize)
    
            self.pos = Position(self)
            self.pos.modx = -8 # para corregir posicion en el eje x
            bt = ttk.Button(self, text='size screen', command=self.pos.toggle)
            bt.pack(expand=True)

        def getSize(self, e=tk.Event) -> None:
            w, h = self.winfo_width(), self.winfo_height()
            self.title(f'{w}x{h}')
    
    
    if __name__ == '__main__':
        vn = VentanaTest()
        vn.mainloop()