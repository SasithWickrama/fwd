import tkinter as tk
from time import sleep
from threading import Thread
from tkinter import ttk
from tkinter import *
site_name =["Nugeoda","Havalock","Rajagiriya","Koswtta","Kirulapana","jaffna","Jawacity","boralas","ganodawila","battara"]
dic ={}
color = ["red","blue","green","yellow","violet"]
count=0
Calbri_font1 = ('Calibri', 13, 'bold')
Calbri_font2 = ('Calibri', 11, 'normal')


def config(mpls_color,pvt_color,pos_x,pos_y):
        global count
       
            
        fram1= tk.Frame(second_frame,background='#03506F')
        fram1.grid(row =pos_x,column=pos_y)


        fram= tk.Frame(fram1,padx=1,pady=1,background='#0A043C')
        fram.grid(padx=4,pady=5)
    
    #fram.grid_propagate(0)
    

        aa = tk.Label(fram,text=num,foreground="black",background="gold",padx=12,width=10,font=Calbri_font1,relief="raised")
        aa.pack(pady=(0,7))
    #num.pack_propagate(False)


        bb= tk.Label(fram,text="Privet",foreground="black",background=pvt_color,width=11,font=Calbri_font2,relief="groove")
        bb.pack(pady=(0,5))

        cc = tk.Label(fram,text="MPLS",foreground="black",background=mpls_color,width=11,font=Calbri_font2,relief="groove")
        cc.pack(pady=(0,8))

            
      


r = 0
c = 0

window = tk.Tk()
window.geometry("400x400")

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

my_canvas = Canvas(window)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar_x =ttk.Scrollbar(window,orient=HORIZONTAL,command=my_canvas.xview)
my_scrollbar_x.place(relx=0,rely=1,relwidth=1,anchor='sw')
my_canvas.configure(xscrollcommand=my_scrollbar_x.set)

my_scrollbar =ttk.Scrollbar(window,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.place(relx=1,rely=0,relheight=1,anchor='ne')
my_canvas.configure(yscrollcommand=my_scrollbar.set)


my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=(my_canvas.bbox("all"))))#my_canvas.bbox("all")

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")#




for num in site_name:

    fram1= tk.Frame(second_frame,background='#03506F')
    fram1.grid(row =r,column=c)


    fram= tk.Frame(fram1,padx=1,pady=1,background='#0A043C')
    fram.grid(padx=4,pady=5)
    
    #fram.grid_propagate(0)
    

    aa = tk.Label(fram,text=num,foreground="black",background="gold",padx=12,width=10,font=Calbri_font1,relief="raised")
    aa.pack(pady=(0,7))
    #num.pack_propagate(False)


    bb= tk.Label(fram,text="Privet",foreground="black",background="green2",width=11,font=Calbri_font2,relief="groove")
    bb.pack(pady=(0,5))

    cc = tk.Label(fram,text="MPLS",foreground="black",background="red2",width=11,font=Calbri_font2,relief="groove")
    cc.pack(pady=(0,8))

    dic[num] =r,c

    r +=1

    if r==5:
        r=0
        c=1


print(dic)

#command=config()

def abcd():
      pass

def abc():
        for x in color:
            config(x,x,2,1)
            sleep(1)
            print(x)  

th = Thread(target=abc)
th.daemon = True
th.start()

window.mainloop()




