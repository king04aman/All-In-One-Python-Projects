from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.geometry("700x500")
root.title("Aman's Notepad")

def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

def clear():
    messagebox.showinfo("Cleared", "Cleared all contents !")
    entry.delete(1.0, END)

def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

b1 = Button(root, text="Save", command=save_file)
b1.place(x=10, y=10)

b2 = Button(root, text="Clear", command=clear)
b2.place(x=70, y=10)

b3 = Button(root, text="Open", command=open_file)
b3.place(x=120, y=10)

entry = Text(root, height=60, width=70, wrap=WORD, bg="black", fg="green", selectbackground="red",
             font="Courier 15", insertbackground="violet")
entry.place(x=10, y=50)

root.mainloop()
