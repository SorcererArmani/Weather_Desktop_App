import tkinter as tk
from types import LambdaType
from tkinter import font
import requests
def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']

        final_str='City: %s \nCondition: %s \nTemperature: %s'%(name, desc, temp)
    except:
        final_str='There was a problem retrieving that information'
    return final_str


def get_weather(city):
   weather_key='43c4b70ab690d82343224b74c098e76b'
   url='https://api.openweathermap.org/data/2.5/weather'
   params={'APPID':weather_key,'q':city,'units':'imperial'}
   response=requests.get(url,params=params)
   weather = response.json()

   label['text']=format_response(weather)


HEIGHT=650
WIDTH=750
root = tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

#background_image=tk.PhotoImage(file='C:\Users\AsuS\OneDrive\Desktop\python\landscape.png')
#background_lable=tk.Label(root,image=background_image)
#background_lable.pack(x=0,y=0,relwidth=1,relheight=1)
#background_lable.pack(row=0,column=0,padx=10,pady=10)


frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry=tk.Entry(frame,bg="white",font=('Courier',18))
#entry.place(side='left',fill='both')
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get Weather",bg="orange",fg="white",font=('Courier',12),command=lambda:get_weather(entry.get()))
#button.place(side='left',fill='x',expand=True)
button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,bg="white",font=('Courier',18),anchor='nw',justify='left')
#label.pack(side='left',fill='both')
label.place(relwidth=1,relheight=1)

print(tk.font.families())
root.mainloop()