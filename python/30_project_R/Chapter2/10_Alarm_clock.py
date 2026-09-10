#import and global variable
import tkinter as tk
from datetime import datetime

window = tk.Tk()

alarm_time = None

window.title("Alarm")
window.resizable(width=False, height=False)
window.geometry("400x300")


# function for getting current time

def get_current_time():
    current_time = datetime.now()

    time_lable.configure(
        text=current_time.strftime("%H:%M:%S")
    )

    window.after(1000, get_current_time)


# function set alarm timer

def set_alarm():
    global alarm_time

    try:
        hour = int(hour_alarm_entry.get())
        minute = int(minute_alarm_entry.get())

        # check valid time
        if hour < 0 or hour > 23:
            latest_alarm_label.configure(text="Invalid hour!")
            return

        if minute < 0 or minute > 59:
            latest_alarm_label.configure(text="Invalid minute!")
            return

        current_time = datetime.now()

        alarm_time = current_time.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )

        # if selected time is already passed,
        # set alarm for tomorrow
        if alarm_time <= current_time:
            from datetime import timedelta
            alarm_time = alarm_time + timedelta(days=1)

        latest_alarm_label.configure(
            text=f"Alarm: {alarm_time.strftime('%H:%M')}"
        )

    except ValueError:
        latest_alarm_label.configure(
            text="Please enter numbers!"
        )


# function for comparing time with alarm

def check_alarm():
    global alarm_time

    if alarm_time is not None:

        current_time = datetime.now()

        if current_time >= alarm_time:
            latest_alarm_label.configure(
                text="ALARM!!!"
            )

            alarm_time = None

    window.after(1000, check_alarm)


# UI design


# text time

time_lable = tk.Label(
    window,
    text="12:30:30",
    font=("Tahoma", 30)
)

time_lable.pack(pady=20)


# text input hour
# input entry

tk.Label(
    window,
    text="hour"
).pack()

hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()


# text input minute
# input entry

tk.Label(
    window,
    text="minute"
).pack()

minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()


# button set alarm

tk.Button(
    window,
    text="set alarm",
    command=set_alarm
).pack(pady=10)


# showing last alarm

latest_alarm_label = tk.Label(
    window,
    text="No alarm set"
)

latest_alarm_label.pack()


# running application

get_current_time()
check_alarm()

window.mainloop()