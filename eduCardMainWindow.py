import tkinter as tk
from tkinter import Canvas
#import csv

def do_quit():
    root.destroy()

def open_csv():
    print("Open CSV clicked")

def next_action():
    print("Next clicked")

def submit_data():
    print("Submit clicked")

def create_widgets(root):
    tk.Button(root, text="Quit", command=do_quit).grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    tk.Button(root, text="Open CSV", command=open_csv).grid(row=0, column=1, sticky='ew', padx=5, pady=5)
    tk.Button(root, text="Next", command=next_action).grid(row=0, column=2, sticky='ew', padx=5, pady=5)

    tk.Label(root, text="Text Label").grid(row=1, column=0, columnspan=3, sticky='ew', padx=5, pady=5)
    
    canvas = Canvas(root, bg="blue")
    canvas.grid(row=2, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)
    
    tk.Entry(root).grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
    tk.Button(root, text="Submit", command=submit_data).grid(row=3, column=2, sticky='ew', padx=5, pady=5)

def main():
    global root
    root = tk.Tk()
    root.title("Scalable Tkinter Example")

    create_widgets(root)

    for i in range(3):  # Only 3 columns used
        root.grid_columnconfigure(i, weight=1)
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
