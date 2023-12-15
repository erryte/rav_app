import tkinter as tk
from tkinter import ttk

selectionbar_color = '#7f7f00'
sidebar_color = '#000000'
header_color = '#008080'
visualisation_frame_color = "#f9f9f9"

class SidebarSubMenu(tk.Frame):
    def __init__(self, parent, sub_menu_heading, sub_menu_options):
        tk.Frame.__init__(self, parent)
        self.config(bg=sidebar_color)
        self.sub_menu_heading_label = tk.Label(self,
                                               text=sub_menu_heading,
                                               bg=sidebar_color,
                                               fg="#f9f9f9",
                                               font=("Helvetica", 10)
                                               )
        self.sub_menu_heading_label.place(x=30, y=10, anchor="w")

        sub_menu_sep = ttk.Separator(self, orient='horizontal')
        sub_menu_sep.place(x=30, y=30, relwidth=0.8, anchor="w")

        self.options = {}
        for n, x in enumerate(sub_menu_options):
            self.options[x] = tk.Button(self,
                                        text=x,
                                        background=sidebar_color,
                                        font=("Helvetica", 12),
                                        bd=0,
                                        cursor='arrow',
                                        activebackground='#000000',
                                        highlightbackground = sidebar_color,  
                                        highlightthickness = 2
                                        )
            self.options[x].place(x=30, y=50 * (n + 1), anchor="w")

