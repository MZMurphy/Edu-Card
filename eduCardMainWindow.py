import tkinter as tk



root=tk.Tk() # Create main window/canvas/root # 'The root of our GUI' 
root.title("EDU-CARD")

def doQuit():
    """Exit and close program"""
    exit()

#
# No functionality to button yet! ! !
#
button1 = tk.Button(text="Quit", width=10, height=2,command=doQuit)
button1.pack()
#button1.place(relx=0.5, rely=0.5, anchor="center") 

#
# No functionality to button yet! ! !
#
button2 = tk.Button(text="Open CSV", width=10, height=2,)
button2.pack()

#
# No functionality to button yet! ! !
#
button3 = tk.Button(text="First", width=10, height=2,)
button3.pack()



root.mainloop()