import tkinter as tk
from tkinter import ttk
from yarnbrands import YarnBrands
from patterns import Patterns
from login import Login
from signup import Signup
from sidebarmenu import SidebarSubMenu
from home import Home

api_token = 'd2c6fb476d706beda8f3dfe6d53a252d4627d696'
api_url_base = 'https://api.ravelry.com'

selectionbar_color = '#f9f9f9'
sidebar_color = '#000000'
header_color = '#008080'
visualisation_frame_color = "#f9f9f9"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Ravelry App') 

        self.geometry("800x500+300+200")
        self.resizable(True, True)
        self.title('Ravelry App')
        self.config(bg=sidebar_color)

        # HEADER
        self.header = tk.Frame(self, bg=header_color)
        self.header.config(
            highlightbackground="#595857",
            highlightthickness=0.2
        )
        self.header.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.1)

        # SIDEBAR
        self.sidebar = tk.Frame(self, bg=sidebar_color)
        self.sidebar.config(
            bg=sidebar_color,
            highlightbackground="#595857",
            highlightthickness=0.5
            )
        self.sidebar.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        # SIDEBAR LOGO AND OPTIONS
        self.brand_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # logo = tk.Label(self.brand_frame, bg=sidebar_color)
        # logo.place(x=5, y=20)
        brand_name = tk.Label(self.brand_frame,
                              text='Ravelry',
                              bg=sidebar_color,
                              fg="white",
                              font=("", 15, 'bold')
                              )
        
        brand_name.place(x=15,y=27,anchor='w')
        brand_name = tk.Label(self.brand_frame,
                              text='App',
                              bg=sidebar_color,
                              fg="white",
                              font=("", 15, 'bold')
                              )
        
        brand_name.place(x=15,y=60,anchor='w')

        # SIDEBAR SUBMENUS
        self.submenu_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.submenu_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.85)

        # SUB - DETAILS
        pages_submenu = SidebarSubMenu(self.submenu_frame,
                                     sub_menu_heading='DETAILS',
                                     sub_menu_options=["Patterns",
                                                       "Yarn brands",
                                                       ]
                                     )
        pages_submenu.options["Patterns"].config(
            command=lambda: self.show_frame(Patterns, "Patterns")          
        )

        pages_submenu.options["Yarn brands"].config(
            command=lambda: self.show_frame(YarnBrands, "Yarn Brands")
        )

        pages_submenu.place(relx=0, rely=0.025, relwidth=1, relheight=0.3)

        # SUB - USER PREFERENCES
        user_submenu = SidebarSubMenu(self.submenu_frame,
                                    sub_menu_heading='USER PREFERENCES',
                                    sub_menu_options=["Login",
                                                      "Sign Up",
                                                      ]
                                    )
        user_submenu.options["Login"].config(
            command=lambda: self.show_frame(Login, "Login")
        )
        user_submenu.options["Sign Up"].config(
            command=lambda: self.show_frame(Signup, "Sign Up")
        )
        user_submenu.place(relx=0, rely=0.4, relwidth=1, relheight=0.3)

        # PAGE CONTENT
        container = tk.Frame(self)
        container.config(highlightbackground="#595857", highlightthickness=0.2)
        container.place(relx=0.3, rely=0.1, relwidth=0.7, relheight=0.9)

        self.frames = {}

        for F in (Home, 
                  Patterns,
                  YarnBrands, 
                  Login,
                  Signup):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_frame(Home, "")
    
    def show_frame(self, cont, title):
        '''
        this function enable us to switch between frames 
        '''
        frame = self.frames[cont]
        for widget in self.header.winfo_children():
            widget.destroy()
        label = tk.Label(self.header,
                         text=title,
                         font=("Helvetica", 17),
                         bg=header_color,
                         fg="#f9f9f9")
        label.pack(side=tk.LEFT, padx=10)
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
