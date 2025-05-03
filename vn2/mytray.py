import threading
from pathlib import Path
from PIL import Image, ImageDraw
from pystray import Icon, MenuItem, Menu


class MyTray:
    def __init__(self, parent, image_icon=None):
        self.parent = parent
        self.img_icon= image_icon
        self.title = "Mi Programa X"
        self.msg = "Hola, mi notificacion."
        self.setImageIcon(self.img_icon)

    def createImage(self, width, height=None) -> Image.Image:
        if not height:
            height = width
        img = Image.new('RGB', (width, height), 'blue')
        img_draw = ImageDraw.Draw(img)
        img_draw.ellipse((0,0,width, height),fill='orange')
        return img
    
    def setImageIcon(self, img=None):
        image = Path(img)
        icon_image = Image.open(image.as_posix()) \
            if image.exists() else self.createImage(64, 64)
        self._setMenu(icon_image)
        
    def _setMenu(self, image=Image.Image):
        self.icon = Icon(
            name="text_icon",
            icon=image,
            title=self.title,
            menu=Menu(
                MenuItem("Restaurar ventana", self.restoreWindow),
                MenuItem("Salir", self.closeWindow)
            )
        )

    def test(self, icon, item):
        print("accion")

    def showNotification(self, msg):
        self.icon.notify(msg)
        
    def run(self):
        threading.Thread(target=self.icon.run, daemon=True).start()

    def stop(self):
        self.icon.stop()

    def closeWindow(self):
        self.icon.stop()
        self.parent.destroy()

    def minimizeWindow(self):
        # self.parent.iconify()
        self.parent.withdraw()  # Minimiza la ventana
        self.showNotification("El programa se encuentra en la bandeja minimizado.")

    def restoreWindow(self):
        self.parent.deiconify()


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

            bt_min = tk.Button(self, text='minimizar', command=self.minimize)
            bt_min.pack(expand=True)
            bt_close = ttk.Button(self, text='cerrar', command=self.close)
            bt_close.pack(expand=True)

            self.tray = MyTray(self, image_icon="image1.png")
            self.tray.run()

        def getSize(self, e=tk.Event) -> None:
            w, h = self.winfo_width(), self.winfo_height()
            self.title(f'{w}x{h}')

        def minimize(self):
            self.tray.minimizeWindow()

        def close(self):
            self.tray.closeWindow()


    vn = VentanaTest()
    vn.mainloop()