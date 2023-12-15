import tkinter as tk
from tkinter import ttk

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        message = tk.Label(self, text="Select an option to see your Ravelry project info here", font=("Helvetica", 16))
        message.place(x=5,y=15,anchor='w')
        message.pack()