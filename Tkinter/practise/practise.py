import tkinter as tk

window = tk.Tk()
window.geometry("300x450")
window.title("Practise")

label = tk.Label(window , text="Practise test")
label.pack(padx = 20 , pady=10)

textbox = tk.Text(window , height = 4)
textbox.pack(padx = 10 , pady=10)

btn = tk.Button(window, text="click me !")
btn.pack(padx = 10)


window.mainloop()