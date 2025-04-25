import tkinter as tk
from tkinter import ttk
import funciones as fun


class Background:
    def __init__(self):
        self.normal = 'gray'
        self.hover = 'gray20'
        self.pressed = 'black'

class Icon:
    def __init__(self):
        self.d = {
            'star': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABqklEQVR4nI2SPW/TUBSGH1vXYCnKcPMhRUqcCSSEQ'\
            'Q1TpiLROE3L1oLZOyLoD4A/ABJiRPwCplZEnWgrkUR0ajpZrZQBMyQOQ6RKaebENgNJZaDGfad7zz3vo3P1HoV43Qeez88fgdP/9'\
            'P6jsq7r57b9LLRtO9R1/RwoX9WoxgBeWZaVNU0T07yHZVlZ4PV1AUYqldpaWqpcFiqVB6TT6S3AiAM8AQ4URRlKKQerq42bmqZdN'\
            'gkhqNfrN6SUA0VRfgKHwFMABdgwDONzo7FGoVBACBHzq9+azWaMRiP297/ged6mCmzWahalUinRvJimWCyyslID2FCBwXA4TDT+r'\
            'bmnrwLvWq2v38/Orh9zr9ej3W79AN6rwEUQBLVms9l3XTfR7Louu7s7/SAIHgEXixQ83/e3HcdJBDiOg+/724AHf+5BOZvNJAIym'\
            'QxE9iEKuJPL5RMB+XwO4O7iHs0tjMY4nU7pdo8JQ6hWqywWSwgNILgKsNfptF9omqaOx2OOjr7NJpPJByA8Oem+XF5+KKSUdDrtA'\
            'NiLm/Ax8Al4A9yO1G8Bb+dv61HDLx4ZfwrScvXVAAAAAElFTkSuQmCC',
            'star-hover': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABi0lEQVR4nJXSu2uTURgG8F8+20ahg0EIVE2KkoItS'\
            'hapIDh1UQehraB/gIIXKthOgkMFpSL1AgrJXh10yOBkiosKot3Ey6RDE906a0sSj0O/kFBtUl84nPfyPM954TkJm8chXIzzAj52w'\
            'P4V2VS/lWc3hKezQqrfCrL/I1AoTAvh1fopTAsobpWcSaes/lxsCay+FAZ2WUNmIziK70mUo8j3fQMq85ckdyRboGQvdy7o279bJ'\
            'Yr8wCJOQwLjRw8q3btMPsf2vs7rrdX48JWrj3j7yUSEiVvnOTLSndzcZnSYm+fAeITK+y/diRvj3WewnMDObZGlx9cNnR3bGrn0m'\
            'jOzvtUbDifiXqa3x5vncwaPj3Ymv1ji1DXLtbpjqDZdqNbqphbK3V9fKFOrm0KVlo2QHdrbXSC3Z33jZt0ucGB4sLtAjBlp1j1ts'\
            '5DsbRW/1nhYIgSuTNL8WLHVv/8lPpbPaSzeFYozQiathge4n0mrFWeE8ryQz2lgU79O4gnmMNTWz+F2PDvRTvgDUTVxI+ziRk0AA'\
            'AAASUVORK5CYII='
        }
        self.normal = 'star'
        self.hover = 'star-hover'

    @property
    def normal(self) -> tk.PhotoImage:
        return self.tk_normal
    
    @normal.setter
    def normal(self, name:str):
        icono = self.d.get(name, None)
        self.tk_normal = tk.PhotoImage(data=icono) if icono else None

    @property
    def hover(self) -> tk.PhotoImage:
        return self.tk_hover
    
    @hover.setter
    def hover(self, name:str):
        icono = self.d.get(name, None)
        self.tk_hover = tk.PhotoImage(data=icono) if icono else None

    def setDict(self, dc:dict):
        """set dictionary of icons"""
        self.d = dc
        

class KButton(tk.Button):
    def __init__(self, parent, *args, **kw):
        super(KButton, self).__init__(master=parent, *args, **kw)
        self._configKButton()

    def _configKButton(self):
        self.bg = Background()
        self.ico = Icon()

        self.reloadStyle()
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)

    def onEnter(self, event:tk.Event):
        self.config(bg=self.bg.hover)
        if self.ico.hover:
            self.config(image=self.ico.hover)

    def onLeave(self, event:tk.Event):
        self.config(bg=self.bg.normal)
        if self.ico.normal:
            self.config(image=self.ico.normal)

    def reloadStyle(self):
        self.config(
            bg=self.bg.normal,
            activebackground=self.bg.pressed,
            highlightbackground=self.bg.hover,
            relief='flat',
            # padx=10,
            # pady=10
        )

    def setKeyName(self, name:str, suffix:str='-hover'):
        """set key name for icon"""
        if name in self.ico.d:
            self.ico.normal = name
            self.ico.hover = f"{name}{suffix}"
            self.config(image=self.ico.normal)
        else:
            raise ValueError(f"Icon '{name}' not found in dictionary.")


class BasicButtons(tk.Frame):
    def __init__(self, parent, **kw):
        super(BasicButtons, self).__init__(master=parent, **kw)
        self._configBasicButtons()
    
    def _configBasicButtons(self):
        self.bt_lr = self._mkButton("lr")
        self.bt_lr.grid(row=0, column=0, sticky='wens')
        self.bt_pin = self._mkButton("lock")
        self.bt_pin.grid(row=0, column=1, sticky='wens')
        self.bt_min = self._mkButton("min")
        self.bt_min.grid(row=0, column=2, sticky='wens')
        self.bt_mm = self._mkButton("max")
        self.bt_mm.grid(row=0, column=3, sticky='wens')
        self.bt_close = self._mkButton("close")
        self.bt_close.grid(row=0, column=4, sticky='wens')
        self.bt_pin.config(command=self._changeIconPin)
        self.bt_lr.config(command=self._changeIconLR)
        self.ONTOP = True
        self.POS_L = True

    def _mkButton(self, name:str) -> KButton:
        """create a button with the given name"""
        btn = KButton(self)
        btn.ico.setDict(fun.getConfig('iconos'))
        btn.setKeyName(name)
        return btn
    
    def _changeIconPin(self):
        """change icon pin"""
        self.bt_pin.setKeyName('unlock') if self.ONTOP \
            else self.bt_pin.setKeyName('lock')
        self.ONTOP = not self.ONTOP

    def _changeIconLR(self):
        """change icon lr"""
        self.bt_lr.setKeyName('lr-right') if self.POS_L \
            else self.bt_lr.setKeyName('lr-hover')
        self.POS_L = not self.POS_L

    def setBg(self, bg:str, hover:str=None, pressed:str=None):
        """set background color"""
        self.config(bg=bg)
        for btn in self.winfo_children():
            btn.config(bg=bg)
            btn.bg.normal = bg
            btn.bg.hover = hover if hover else bg
            btn.bg.pressed = pressed if pressed else bg
            btn.reloadStyle()

if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('400x220')

    # TEST BOTON CERRAR
    # wg = KButton(vn)
    # wg.grid(row=0, column=0, sticky='wens')
    # wg.ico.setDict(fun.getConfig('iconos'))
    # wg.setKeyName('close')

    # TEST BOTONES BASICOS
    wg = BasicButtons(vn)
    wg.grid(row=0, column=0, sticky='wens')
    wg.setBg("gray30", "gray", "gray10")


    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()