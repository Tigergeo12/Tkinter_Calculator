import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create the input field
        input_frame = tk.Frame(self.root)
        input_frame.pack()
        
        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        input_field.grid(row=0, column=0, columnspan=4)
        
        # Create buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        
        row_val = 0
        col_val = 0
        
        for button in buttons:
            if button == '=':
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate)
            elif button == 'C':
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=self.clear)
            else:
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.append_to_expression(b))
            
            btn.grid(row=row_val, column=col_val)
            col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1
        
    def append_to_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)
        
    def clear(self):
        self.expression = ""
        self.input_text.set(self.expression)
        
    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.input_text.set(self.expression)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()