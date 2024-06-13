from tkinter import *
from tkinter import font as tkFont
import os

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        for i in range(3):
            Frame.columnconfigure(self, index = i, weight=1)

        Frame.rowconfigure(self, index = 1, weight=1)
        font = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        
        Label(Frame, text='Top left').grid(row=0, column=0, sticky='w')
        Label(Frame, text='Top center').grid(row=0, column=1)
        Label(Frame, text='Top right').grid(row=0, column=2, sticky='e')
        Label(Frame, text='Center').grid(row=1, column=1)
        # Button(master, text='Beenden', font=font, command = self.closeGame).grid(
        #     row=0, column=0)

        # Button(master, text='vs. Computer', font=font, command = self.closeGame).grid(
        #     row=1, column=2
        # )
    pass

    def closeGame(self):
        os._exit(0)