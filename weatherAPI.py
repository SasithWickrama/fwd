import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *

#O4pnvme6fnUJJbqPB8G2ANbIkzpQ8PUo
#hBzXNNfaE8akmmi1GQGeHNVZgIabQnbN
Calbri_font1 = ('Calibri', 13, 'bold')
Calbri_font2 = ('Calibri', 11, 'normal')
list =[0]

def action():

    if ((click.get())=='Set_Point') or ((click_t.get()) =='Set_Point'):
        wann.config(fg="red2",font=Calbri_font1)
        wann.config(text="Please select the Set_point Value")

    else:

        r,t=call_weather()
        #r =50
        #t=50
        rain_val.config(text=f'{r}%')
        th_val.config(text=f'{t}%')

        if (t > int(click_t.get()) ):
            if(r>int(click.get())):
                wann.config(fg="green4",font=Calbri_font1)
                wann.config(text="SMS Pogress has been Started....")
                # sms cording here


                print(click.get())
                print(click_t.get())
            else:
                wann.config(fg="red2",font=Calbri_font1)
                wann.config(text="Rain Set point have less value....")
        else:
            wann.config(fg="red2",font=Calbri_font1)
            wann.config(text="Thunder Set point have less value....")    
            

        

            


def call_weather():

    response = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/311399?apikey=O4pnvme6fnUJJbqPB8G2ANbIkzpQ8PUo&details=true")
    print ("status:",response.status_code)
    jstring = response.json()
    rain=jstring["DailyForecasts"][0]["Day"]["PrecipitationProbability"]
    #print(f'PrecipitationProbability: {rain}%')
    Thunder=jstring["DailyForecasts"][0]["Day"]["ThunderstormProbability"]
    #print(f'ThunderstormProbability: {Thunder}%')
    return rain,Thunder

bg_color = 'lightblue'

window = tk.Tk()
window.geometry("400x230")
window['bg']= bg_color

options_r =[10,20,30,40,50,60,70]
options_t =[10,20,30,40,50,60,70]


click = StringVar()
click.set("Set_Point")


click_t = StringVar()
click_t.set("Set_Point")

fram= tk.Frame(window,padx=1,pady=1,background=bg_color)
fram.place(x=100,y=10)
                    
aa = tk.Label(fram,text='SMS Weather Forcast Portal',bg='deepskyblue',padx=12,width=20,relief="raised",font=Calbri_font1)
aa.pack(pady=(0,7))

fram2= tk.Frame(window,padx=1,pady=1,background=bg_color,borderwidth=2,border=1)
fram2.place(x=10,y=80)

rain= tk.Label(fram2,text='Precipitation_Probability :',padx=10,pady=5,width=20,height=1,relief="raised",font=Calbri_font1)
rain.pack(pady=(0,25))

th= tk.Label(fram2,text='Thunderstorm_Probability:',padx=10,pady=5,width=20,height=1,relief="raised",font=Calbri_font1)
th.pack(pady=(0,7))


fram3= tk.Frame(window,padx=1,pady=1,background=bg_color)
fram3.place(x=240,y=85)

rain_val= tk.Label(fram3,text='0%',padx=7,width=3,relief="raised",font=Calbri_font1)
rain_val.pack(pady=(0,34))

th_val= tk.Label(fram3,text='0%',padx=7,width=3,relief="raised",font=Calbri_font1)
th_val.pack(pady=(0,6))

fram4= tk.Frame(window,padx=1,pady=1,background=bg_color)
fram4.place(x=300,y=85)

dp_r=OptionMenu(fram4,click,*options_r)
dp_r.pack(pady=(0,30))

dp_t=OptionMenu(fram4,click_t,*options_t)
dp_t.pack(pady=(0,12))

bt= tk.Button(window,padx=1,pady=1,background='darkgray',width=10,text='RUN',command=action)
bt.place(x=300,y=185)

wann = tk.Label(window,text="",font=Calbri_font2,fg='green',background=bg_color)
wann.place(x=10,y=190)




window.mainloop()
