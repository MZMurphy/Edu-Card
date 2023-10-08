import tkinter as tk

root = tk.Tk()
root.title("EDU-CARD")

# Make frame for buttons and grid to root
buttonFrame = tk.Frame(root)
buttonFrame.grid(row=0, column=0)

# Config root rows and cols to be resizeable
root.rowconfigure(index=0, weight=1)  # Make row 0 resizable
root.rowconfigure(index=1, weight=1) 
root.columnconfigure(index=0, weight=1)  # Make column 0 resizable

# Config buttonFrame rows and cols to be resizeable
buttonFrame.rowconfigure(index=0, weight=1)
buttonFrame.columnconfigure(index=0, weight=1)
buttonFrame.columnconfigure(index=1, weight=1)
buttonFrame.columnconfigure(index=2, weight=1)

# Create a buttons
button1 = tk.Button(buttonFrame, text="Button 1")
button2 = tk.Button(buttonFrame, text="Button 2")
button3 = tk.Button(buttonFrame, text="Button 3")

# Grid buttons to buttonFrame 
button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=0, column=2, sticky="nsew")

# Set minimum size for rows and columns
root.rowconfigure(0, minsize=50)  # Set the minimum height for row 0
root.rowconfigure(1, minsize=50)  # Set the minimum height for row 1
root.columnconfigure(0, minsize=100)  # Set the minimum width for column 0
root.columnconfigure(1, minsize=100)  # Set the minimum width for column 1
root.columnconfigure(2, minsize=100)  # Set the minimum width for column 2

# Create canvasframe and grid to root
canvasframe = tk.Frame(root)
canvasframe.grid(row=1, column=0, sticky="nsew") # Not an issue to use grid as not in same container as pack usage 

# Set the maximum size for the canvas based on the size of canvasframe
canvasframe.grid_rowconfigure(0, weight=1)
canvasframe.grid_columnconfigure(0, weight=1)

# Create canvas and pack to cavasFrame
canvas = tk.Canvas(canvasframe, bg='blue')
canvas.grid(row=0, column=0, sticky="nsew")

# Create a rectangle that fills the canvas
canvas.create_rectangle(0, 0, canvas.winfo_reqwidth(), canvas.winfo_reqheight(), fill="red")  # Set the maximum size for the canvas

# Set minimum size for rows and columns in the frame
canvasframe.rowconfigure(0, weight=1)
canvasframe.columnconfigure(0, weight=1)

root.mainloop()