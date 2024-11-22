import tkinter as tk

calculation = ""

def addToCalc(char):
    global calculation #global variable that can be accessed everywhere
    calculation = calculation + str(char) 
    text_res.delete(1.0 , "end") #from line 1 character 0 to the end 
    text_res.insert(1.0 , calculation) # syntax of insert(where to insert , what to insert)

def Eval():
    pass

def C():
    pass

window = tk.Tk()
window.geometry("375x450")

text_res = tk.Text(window , height=2 , width = 20 , font = ("Futura" , 24))
text_res.grid(columnspan = 5)
window.mainloop()
