from tkinter import *

class Input:
    def __init__(self):
        w = Tk()
        e= Entry(w)
        e.pack()
        e.focus_set()
        def input():
            w.destroy()
            return e.get()
        
        b = Button(w, text = "OK", width = 10, command = input)
        b.pack()
        mainloop()
        
    
        
        
print(Input())