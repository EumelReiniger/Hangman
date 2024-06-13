from tkinter import *
import os

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        Button(master, text='O  Beenden', width=10, command = self.action).grid(
            row = 3, column = 0, sticky = W, pady = 4
        )
    pass

    def action(self):
        os._exit(0)