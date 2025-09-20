from time import strftime
from tkinter import Label, Tk , Button

window = Tk()
window.title("Digital Clock")
window.geometry("300x100")
window.configure(bg="green")
window.resizable(False, False) 

use_24h = True

clock_label = Label(
    window, bg="black", fg="green", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=50, y=50)


date_label = Label(
    window, bg="black", fg="white", font=("Arial", 14)
)
date_label.pack(pady=(0, 10), anchor="center")



def toggle_format(_evt=None):
    global use_24h
    use_24h = not use_24h
    fmt_btn.config(text="Switch to 24-hour" if not use_24h else "Switch to 12-hour")

fmt_btn = Button(window, text="Switch to 12-hour", command=toggle_format)
fmt_btn.pack(pady=(0, 8))
window.bind("<f>", toggle_format)  # press 'f' to toggle



def update_label():
    
    if use_24h:
        time_text = strftime("%H:%M:%S")
    else:
        # strip leading zero in 12h mode for a cleaner look
        time_text = strftime("%I:%M:%S %p").lstrip("0")
    clock_label.configure(text=time_text)
    date_label.configure(text=strftime("%A, %b %d, %Y"))
    window.after(1000, update_label)

update_label()
window.mainloop()


