from Application import Application
from tkinter import *

root = Tk()
root.pack_propagate(0)
root.geometry("800x800")
root.resizable(0, 0)
app = Application(master = root)
app.mainloop()