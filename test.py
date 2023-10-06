import tkinter as tk

root = tk.Tk()
root.title("EDU-CARD")

# Make rows and columns resizable / Configure our rows and cols to be resizeable
root.rowconfigure(0, weight=1)  # Make row 0 resizable
root.rowconfigure(1, weight=1)  # Make row 1 resizable
root.columnconfigure(index=0, weight=1)  # Make column 0 resizable
root.columnconfigure(index=1, weight=1)  # Make column 1 resizable
root.columnconfigure(index=2, weight=1)  # Make column 2 resizable

# Create a buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Could create another frame to stop button 2 from resizing with the canvas, but I actually like it better this way. 

# Grid buttons to root/screen 
button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=0, column=2, sticky="nsew")

# Set minimum size for rows and columns
root.rowconfigure(0, minsize=50)  # Set the minimum height for row 0
root.rowconfigure(1, minsize=50)  # Set the minimum height for row 1
root.columnconfigure(0, minsize=100)  # Set the minimum width for column 0
root.columnconfigure(1, minsize=100)  # Set the minimum width for column 1
root.columnconfigure(2, minsize=100)  # Set the minimum width for column 2

# Create frame
frame = tk.Frame(root, width=640, height=420)

# Grid frame to root/screen
frame.grid(row=1, column=1,) # Not an issue to use grid as not in same container as pack usage 

# Create canvas
canvas = tk.Canvas(frame, width=620, height=400, bg='blue')

# Grid canvas to frame
canvas.pack()

# Create question box
questionBox =tk.Label(text="") # Font not specified

root.mainloop()