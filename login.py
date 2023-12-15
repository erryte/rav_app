import tkinter as tk
from tkinter import ttk

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login", font=("Helvetica", 16))
        label.pack()