#import and global variable
import tkinter as tk
window = tk.Tk()
window.title("Alarm")
window.resizable(width=False,height=False)
window.geometry("400x300")
#function for getiing current time


 

#function set alarm timer

def set_alarm():
    print("alarm has been set",hour_alarm_entry.get(),minute_alarm_entry.get())



#function  for comparing time  with alarm


# UI design


#text time

time_lable = tk.Label(window,text="12:30:30",font=("Tahoma"))
time_lable.pack()


#text input hour
#input entrt

tk.Label(window,text='hour').pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()


#text input minute
#input entry
tk.Label(window,text='minute').pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()

#button set alarm 

tk.Button(window,text="set alarm",command=set_alarm).pack()


#showing last alarm 

latest_alarm_label = tk.Label(window,text="12:31")
latest_alarm_label.pack()


#running application
window.mainloop()