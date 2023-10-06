import tkinter as tk

root = tk.Tk()
root.title("EDU-CARD")

# Make rows and columns resizable
root.rowconfigure(0, weight=1)  # Make row 0 resizable
root.rowconfigure(1, weight=1)  # Make row 1 resizable
root.columnconfigure(0, weight=1)  # Make column 0 resizable
root.columnconfigure(1, weight=1)  # Make column 1 resizable
root.columnconfigure(2, weight=1)  # Make column 2 resizable

# Create buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Grid buttons to root/screen
button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=0, column=2, sticky="nsew")

# Set minimum size for rows and columns
root.rowconfigure(0, minsize=50)  # Set the minimum height for row 0
root.columnconfigure(0, minsize=100)  # Set the minimum width for column 0
root.columnconfigure(1, minsize=100)  # Set the minimum width for column 1
root.columnconfigure(2, minsize=100)  # Set the minimum width for column 2

# Create frame for canvas
frame = tk.Frame(root)
frame.grid(row=1, column=1, sticky="nsew")

# Create canvas within the frame
canvas = tk.Canvas(frame, bg='blue')
canvas.grid(row=0, column=0, sticky="nsew")

# Set maximum size for the canvas
#canvas.create_rectangle(0, 0, 620, 400)  # Set the maximum size for the canvas
canvas.create_rectangle(0, 0, frame.winfo_reqwidth(), frame.winfo_reqheight())  # Set the maximum size for the canvas

# Set minimum size for rows and columns in the frame
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Create question box
questionBox = tk.Label(text="")  # Font not specified

root.mainloop()
