import requests
import urllib
from urllib.parse import urlparse
from requests.auth import HTTPBasicAuth
from json import JSONDecodeError
import tkinter as tk
from tkinter import ttk
from extract import json_extract


api_token = 'd2c6fb476d706beda8f3dfe6d53a252d4627d696'
api_url_base = 'https://api.ravelry.com'

class YarnBrands(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Get yarn brands for username:", font=("Helvetica", 16))
        label.pack()      
        
        self.pack(fill=tk.BOTH, expand=True)
        self.entry = tk.Entry(self)
        self.entry.focus()
        self.entry.label = tk.Label()
        self.entry.pack()
        self.button = tk.Button(self, text="Submit", command=self.get_button)
        self.button.pack()

        self.text_box = tk.Text(self)
        self.text_box.place(relx=0.5, rely=0.5, anchor='center')
        self.text_box.pack() 
  
    def get_button(self):
        self.entry.get()
        url = api_url_base+"/projects/"+str(self.entry.get())+"/progress.json/"
        parameters = { 
            "key": api_token,
        }
        
        try:
            response = requests.get(url, params=parameters)
            data = response.json()   
            projects = data['projects']
            brands = (json_extract(projects, 'brand'))

            self.text_box.delete('1.0', tk.END) 
            self.text_box.insert('1.0', '\n'.join(brands))
        except JSONDecodeError:
            print('Response could not be serialized') 
            self.text_box.delete('1.0', tk.END) 