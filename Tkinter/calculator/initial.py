import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x700")
        self.window.title("Calculator")

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.current_expression = ""
        self.label = self.create_numbers_label()

        self.create_digit_buttons()
        self.create_operation_buttons()

    def create_numbers_label(self):
        label = tk.Label(self.display_frame, text=self.current_expression, font=("Arial", 24), anchor='e')
        label.pack(expand=True, fill="both")
        return label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=100)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack()
        return frame

    def create_digit_buttons(self):
        self.create_digit_button("1", 3, 1, self.add_one)
        self.create_digit_button("2", 3, 2, self.add_two)
        self.create_digit_button("3", 3, 3, self.add_three)
        self.create_digit_button("4", 2, 1, self.add_four)
        self.create_digit_button("5", 2, 2, self.add_five)
        self.create_digit_button("6", 2, 3, self.add_six)
        self.create_digit_button("7", 1, 1, self.add_seven)
        self.create_digit_button("8", 1, 2, self.add_eight)
        self.create_digit_button("9", 1, 3, self.add_nine)
        self.create_digit_button("0", 4, 2, self.add_zero)
        self.create_digit_button(".", 4, 1, self.add_dot)

    def create_digit_button(self, value, row, column, command):
        button = tk.Button(self.buttons_frame, text=value, command=command)
        button.grid(row=row, column=column)

    def create_operation_buttons(self):
        self.create_operation_button('+', 1, 4, self.add)
        self.create_operation_button('-', 2, 4, self.subtract)
        self.create_operation_button('*', 3, 4, self.multiply)
        self.create_operation_button('/', 4, 4, self.divide)
        self.create_operation_button('=', 5, 4, self.calculate)
        self.create_operation_button('C', 5, 3, self.clear)

    def create_operation_button(self, operation, row, column, command):
        button = tk.Button(self.buttons_frame, text=operation, command=command)
        button.grid(row=row, column=column)

    def add_one(self):
        self.add_to_expression("1")

    def add_two(self):
        self.add_to_expression("2")

    def add_three(self):
        self.add_to_expression("3")

    def add_four(self):
        self.add_to_expression("4")

    def add_five(self):
        self.add_to_expression("5")

    def add_six(self):
        self.add_to_expression("6")

    def add_seven(self):
        self.add_to_expression("7")

    def add_eight(self):
        self.add_to_expression("8")

    def add_nine(self):
        self.add_to_expression("9")

    def add_zero(self):
        self.add_to_expression("0")

    def add_dot(self):
        self.add_to_expression(".")

    def add(self):
        self.add_to_expression("+")
    
    def subtract(self):
        self.add_to_expression("-")

    def multiply(self):
        self.add_to_expression("*")

    def divide(self):
        self.add_to_expression("/")

    def calculate(self):
        num1 = 0
        num2 = 0
        operator = ""

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        self.current_expression = str(result)

    def clear(self):
        self.current_expression = ""
        self.update_label()

    def add_to_expression(self, value):
        self.current_expression += value
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()

calc = Calculator()
calc.run()