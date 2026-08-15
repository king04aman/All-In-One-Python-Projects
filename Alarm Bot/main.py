from tkinter import *
import datetime
import time
import winsound
from threading import *
import os  # Add this to check if sound file exists

root = Tk()
root.geometry("400x250")

# Global variable to control alarm state
alarm_active = False

def stop_alarm():
    """Stop the ringing alarm"""
    global alarm_active
    alarm_active = False
    winsound.PlaySound(None, winsound.SND_ASYNC)
    print("Alarm stopped!")

def play_alarm_sound():
    """Play alarm sound or show visual alert if sound file missing"""
    try:
        # Check if sound.wav exists
        if os.path.exists("sound.wav"):
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        else:
            # If no sound file, print a visual alarm
            print("ALARM! ALARM! ")
            # Make the window flash or show a message
            root.title("ALARM RINGING!")
            # Beep as fallback (Windows only)
            winsound.Beep(1000, 500)  # 1000 Hz for 500ms
    except Exception as e:
        print(f"🔔ALARM RINGING! (Sound error: {e})")

def Threading():
    """Start the alarm in a separate thread"""
    global alarm_active
    alarm_active = True
    t1 = Thread(target=alarm)
    t1.daemon = True
    t1.start()

def alarm():
    """Check time and trigger alarm when it matches set time"""
    global alarm_active
    
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"⏰ Current: {current_time} | Set: {set_alarm_time}")

        if current_time == set_alarm_time:
            print("IT'S TIME!")
            
            # Ring the alarm in a loop until stopped
            ring_count = 0
            while alarm_active and ring_count < 10:  # Ring 10 times
                play_alarm_sound()
                time.sleep(1)
                ring_count += 1
            
            # Reset alarm state
            if alarm_active:
                alarm_active = False
                root.title("Alarm Clock")
                print("Alarm finished (10 rings)")

def update_title():
    """Update window title when alarm is ringing"""
    if alarm_active:
        root.title("ALARM RINGING!")
    else:
        root.title("Alarm Clock")

# UI Setup
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

# Hour dropdown
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Minute dropdown
minute = StringVar(root)
minutes = tuple(f"{i:02d}" for i in range(61))
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Second dropdown
second = StringVar(root)
seconds = tuple(f"{i:02d}" for i in range(61))
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Buttons
Button(root, text="Set Alarm", font=("Helvetica 15"), 
       command=Threading, bg="green", fg="white").pack(pady=10)
Button(root, text="Stop Alarm", font=("Helvetica 15"), 
       command=stop_alarm, bg="red", fg="white").pack(pady=5)

root.mainloop()