import tkinter as tk
from tkinter import ttk

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Signup", font=("Helvetica", 16))
        label.pack()