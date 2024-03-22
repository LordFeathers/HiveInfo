import webbrowser
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hive Profile")
root.iconbitmap("icon.ico")

window_width = 600
window_height = 400
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{left}+{top}")
root.minsize(250,150)

frame0 = ttk.Frame(root)
frame0.pack(expand=True)

label = ttk.Label(frame0, font=30, text="Enter your Hive username")
label.pack()

frame1 = ttk.Frame(frame0)
frame1.pack(pady=0)

username = tk.StringVar()
entry = ttk.Entry(frame1, textvariable=username)
entry.pack(pady=10, side="left")

def open_thing():
    webbrowser.open(f"https://playhive.com/profile/{username.get()}")

button = ttk.Button(frame1, text="Enter", command=open_thing, state="disabled")
button.pack(pady=10)

credits = ttk.Label(root, font=30, text="Created by LordFeathers with much assistance from DirtyPotato")
credits.pack(pady=5)

def on_entry_key(*args):
    if username.get():
        button.config(state="normal")
    else:
        button.config(state="disabled")

entry.bind("<KeyRelease>", on_entry_key)

entry.bind("<Return>", lambda x: button.invoke())

root.mainloop()