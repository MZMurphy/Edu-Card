import tkinter as tk
from tkinter import Canvas

def doQuit():
    """Exit and close program"""
    exit()

root = tk.Tk()
root.title("Scalable Tkinter Example")

# Create three buttons in the top row and columns 1, 2, and 3
button1 = tk.Button(root, text="Quit", command=doQuit) # Add function to button
button1.grid(row=0, column=0, sticky='ew')
 
button2 = tk.Button(root, text="Open CSV") # Add function to button
button2.grid(row=0, column=1, sticky='ew')

button3 = tk.Button(root, text="Next") # Add function to button
button3.grid(row=0, column=2, sticky='ew')

# Create a label to display text
text_label = tk.Label(root, text="Text Label")
text_label.grid(row=1, column=0, columnspan=3, sticky='ew')

# Create a canvas for displaying an image
canvas = Canvas(root, bg="blue")
canvas.grid(row=2, column=0, columnspan=3, sticky='nsew')

# Create a text input box
input_box = tk.Entry(root)
input_box.grid(row=3, column=0, columnspan=2, sticky='ew')

# Create a button for data submission
submit_button = tk.Button(root, text="Submit") # Add function to button
submit_button.grid(row=3, column=2, sticky='ew')

# Make the columns and rows expand when the window is resized
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()