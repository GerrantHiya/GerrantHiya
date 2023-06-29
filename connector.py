import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from tkinter import ttk
from tkinter.font import Font
import datetime
from datetime import datetime

# database connection

dbc = mysql.connector.connect(
    host = 'localhost',
    user = 'user',
    password = '6Vmv-Jl/Sba4F9jM',
    database = 'data_sales'
)
print("================PROGRAM LOGS================")

now = datetime.now()
nowDate = now.strftime("%Y-%m-%d")
thn = now.year
thn_b = now.strftime("%y")
tgl = now.strftime("%d")
bln = now.strftime("%m")
nowtime = now.strftime("%H:%M:%S")
logs = f"[{nowDate}]"

if dbc.is_connected():
    print(f"[{nowDate}] Database connected")
    print(f"[{nowDate}] Program is Running")
    #messagebox.showinfo(title="MySQL Connected!", message="Connected!")
else:
    print("Error!")
    messagebox.showerror(title="MySQL isn't Connected!", message="Check your MySQL Connection!")
