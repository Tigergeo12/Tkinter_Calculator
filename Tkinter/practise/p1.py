import tkinter as tk

window = tk.Tk()
window.geometry("300x450")
window.title("Practise")

label = tk.Label(window , text="Practise test")
label.pack(padx = 20 , pady=10)

textbox = tk.Text(window , height = 4)
textbox.pack(padx = 10 , pady=10)

buttonsFrame = tk.Frame(window)
buttonsFrame.columnconfigure(0 , weight=1)
buttonsFrame.columnconfigure(1 , weight=1)
buttonsFrame.columnconfigure(2 , weight=1)
buttonsFrame.columnconfigure(3 , weight=1)

btn1 = tk.Button(buttonsFrame , text="1" , font=("Futura" , 18))
btn1.grid(row = 0 , column = 0 , sticky=tk.W+tk.E)

btn2 = tk.Button(buttonsFrame , text="2" , font=("Futura" , 18))
btn2.grid(row = 0 , column = 1 , sticky=tk.W+tk.E)

btn3 = tk.Button(buttonsFrame , text="3" , font=("Futura" , 18))
btn3.grid(row = 0 , column = 2 , sticky=tk.W+tk.E)

btn4 = tk.Button(buttonsFrame , text="4" , font=("Futura" , 18))
btn4.grid(row = 1 , column = 0 , sticky=tk.W+tk.E)

btn5 = tk.Button(buttonsFrame , text="5" , font=("Futura" , 18))
btn5.grid(row = 1 , column = 1 , sticky=tk.W+tk.E)

btn6 = tk.Button(buttonsFrame , text="6" , font=("Futura" , 18))
btn6.grid(row = 1 , column = 2 , sticky=tk.W+tk.E)

btn7 = tk.Button(buttonsFrame , text="7" , font=("Futura" , 18))
btn7.grid(row = 2 , column = 0 , sticky=tk.W+tk.E)

btn8 = tk.Button(buttonsFrame , text="8" , font=("Futura" , 18))
btn8.grid(row = 2 , column = 1 , sticky=tk.W+tk.E)

btn9 = tk.Button(buttonsFrame , text="9" , font=("Futura" , 18))
btn9.grid(row = 2 , column = 2 , sticky=tk.W+tk.E )

buttonsFrame.pack(fill="x")
window.mainloop()