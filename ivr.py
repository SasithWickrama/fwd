import tkinter as tk
from time import sleep
from threading import Thread
from tkinter import ttk
from tkinter import *
import requests

Calbri_font1 = ('Calibri', 13, 'bold')
Calbri_font2 = ('Calibri', 11, 'normal')

class api():

    def action(self):
    
        url = "https://172.25.40.144/fault_verification/api.php"

        data = {
            "phone_number": self,
            "UID": "8787",
            "secret_code": "abc123"
    }

        headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

# Use the 'data' parameter to send the data in the request body
        response = requests.post(url, data=data, headers=headers, verify=False)

# Print the response content
        print(response.text)


def action():
    print(ef_1.get())
    print(ef_2.get())
    api.action(ef_1.get())
def table():
    print("bjkbb.bj,b,")
    for x in range(5):# row
        for y in range(2):

            frameGrid = tk.Frame(
            window,
            relief=tk.RAISED,
            borderwidth=2,
            bg='skyblue'

            )
            frameGrid.grid(row=x, column=y)
            labelGrid = tk.Label(frameGrid, text=f"Row No. {x}\nColumn No. {y}",bg='skyblue')
            labelGrid.pack()
            #labelGrid .place(x=0,y=0)
            

            

window = tk.Tk()
window.geometry("400x250")
window['bg']='skyblue'

headline= tk.Label(window,text=' IVR_SYSTEM_PORTAL :',padx=7,width=15,font=Calbri_font1,fg='red2',bg='skyblue')
headline.place(x=150,y=20)

fram3= tk.Frame(window,padx=1,pady=1,background='skyblue')
fram3.place(x=0,y=85)

rain_val= tk.Label(fram3,text='Telephone_Num :',padx=7,width=15,relief="raised",font=Calbri_font1,bg="green2")
rain_val.pack(pady=(0,34))

th_val= tk.Label(fram3,text='Mobile_Num :',padx=7,width=15,relief="raised",font=Calbri_font1,bg="red2")
th_val.pack(pady=(0,6))

entry= tk.Frame(window,padx=1,pady=1,background='skyblue')
entry.place(x=200,y=85)

ef_1 = Entry(entry, bd =5)
ef_1.pack(pady=(0,34))

ef_2 = Entry(entry, bd =5)
ef_2.pack(pady=(0,34))

bt= tk.Button(window,padx=1,pady=1,background='darkgray',width=8,text='CALL',command=action)
bt.place(x=200,y=185)

load= tk.Button(window,padx=1,pady=1,background='darkgray',width=8,text='TABLE',command=table)
load.place(x=270,y=185)

mess= tk.Label(window,text='message',padx=7,width=15,font=Calbri_font1,fg='red2',bg='skyblue')
mess.place(x=0,y=200)

window.mainloop()