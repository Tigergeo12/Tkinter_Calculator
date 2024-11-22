import tkinter as tk # we dont import the whole lobrary because we dont need everything and this is considered to be good practise

class Calculator: # calss
    def __init__(self): #__init__ is an already made function in python and it is basiaclly the same as a javascriupt constructor
        # Initialize the main window
        self.window = tk.Tk() #creates the windwo
        self.window.geometry("400x600") # THe dimensions of the calculator
        self.window.title("Calculator") #title thats at the top of the window

        # Initialize calculator state
        self.current_value = 0  # Stores the initial value
        self.current_operator = None  # Stores the selected operator
        self.is_new_entry = True  # Tracks if the current input is new (after an operator or result)

        # Create display and button frames
        self.display_frame = self.create_display_frame() # here we split the window into 2 parts or frames the display and buttons frame
        self.label = self.create_display_label() # label is the display or we can call the textbox where everything will be
        self.buttons_frame = self.create_buttons_frame() # the frame for buttons
 
        # Add buttons manually function
        self.create_buttons()

    # Create the frame for the display area
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=100, bg="lightgray") # first parameter is the master (in our case window because thats where were puitting the frame) , parameters after this are for looks or geomety
        frame.pack(expand=True, fill="both") #first parameter is so that it expands fully second is that it fills both the x and y axis
        return frame #returs the frame

    # Create the label that shows the current input or result
    def create_display_label(self): 
        label = tk.Label(self.display_frame, text="0", font=("Arial", 24), anchor='e', bg="white") #as usual the first parameter is its master here the label is inside the display frame so display frame is its master (display frames master is window)
        label.pack(expand=True, fill="both") #same as before
        return label #returns

    # Create the frame for the calculator buttons
    def create_buttons_frame(self): 
        frame = tk.Frame(self.window) #creating it and putting window as master
        frame.pack(expand=True, fill="both") # i didnt mention before pack is what actually adds it to the master here we can also but padding for it or add anything for looks
        return frame # returns the button frame

    # Add calculator buttons manually
    def create_buttons(self):
        # Row 1: 7, 8, 9, /
        tk.Button(self.buttons_frame, text="7", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("7")).grid(row=0, column=0, sticky="nsew") #sticky is used for coordinates nsew are north south east west if you use all its just going to be centered
        tk.Button(self.buttons_frame, text="8", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("8")).grid(row=0, column=1, sticky="nsew")
        tk.Button(self.buttons_frame, text="9", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("9")).grid(row=0, column=2, sticky="nsew")
        tk.Button(self.buttons_frame, text="/", font=("Arial", 18), bg="orange", command=lambda: self.set_operator("/")).grid(row=0, column=3, sticky="nsew")

        # Row 2: 4, 5, 6, *
        tk.Button(self.buttons_frame, text="4", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("4")).grid(row=1, column=0, sticky="nsew")
        tk.Button(self.buttons_frame, text="5", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("5")).grid(row=1, column=1, sticky="nsew")
        tk.Button(self.buttons_frame, text="6", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("6")).grid(row=1, column=2, sticky="nsew")
        tk.Button(self.buttons_frame, text="*", font=("Arial", 18), bg="orange", command=lambda: self.set_operator("*")).grid(row=1, column=3, sticky="nsew")

        # Row 3: 1, 2, 3, -
        tk.Button(self.buttons_frame, text="1", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("1")).grid(row=2, column=0, sticky="nsew")
        tk.Button(self.buttons_frame, text="2", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("2")).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.buttons_frame, text="3", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("3")).grid(row=2, column=2, sticky="nsew")
        tk.Button(self.buttons_frame, text="-", font=("Arial", 18), bg="orange", command=lambda: self.set_operator("-")).grid(row=2, column=3, sticky="nsew")

        # Row 4: C, 0, =, +
        tk.Button(self.buttons_frame, text="C", font=("Arial", 18), bg="red", command=self.clear).grid(row=3, column=0, sticky="nsew")
        tk.Button(self.buttons_frame, text="0", font=("Arial", 18), bg="lightblue", command=lambda: self.add_to_expression("0")).grid(row=3, column=1, sticky="nsew")
        tk.Button(self.buttons_frame, text="=", font=("Arial", 18), bg="green", command=self.calculate).grid(row=3, column=2, sticky="nsew")
        tk.Button(self.buttons_frame, text="+", font=("Arial", 18), bg="orange", command=lambda: self.set_operator("+")).grid(row=3, column=3, sticky="nsew")

        # Configure grid weights for uniform button sizes
        for i in range(4):
            self.buttons_frame.rowconfigure(i, weight=1) #expands the rows so that its uses the full space of the frame gives each element weight 1 and total is 4
            self.buttons_frame.columnconfigure(i, weight=1) #same it expands columns so that the frame is filler

    # Handle digit button clicks
    def add_to_expression(self, value):
        if self.is_new_entry: # makes it so that you can actually use 2 digit numbers and not every press is taken into as a new caclculation
            self.label.config(text=value)  # Replace the current display if it's a new entry
            self.is_new_entry = False #so that you can use multiple DIGIT NUMBERS
        else:
            current_text = self.label["text"] #just appnding text
            self.label.config(text=current_text + value)  # Append the digit to the display

    # Handle operator button clicks
    def set_operator(self, operator):
        self.current_operator = operator  # stores operator
        self.current_value = int(self.label["text"])  # Store the first num
        self.is_new_entry = True  # Reset for the next number 

    # Perform the calculation
    def calculate(self):
        if not self.current_operator: # if u dont select operator nothing happens
            return  # If no operator was set, do nothing
        second_value = int(self.label["text"])  # Get the second value

        if self.current_operator == "+": #ubralo advili kalkulatoris kodi
            result = self.current_value + second_value
        elif self.current_operator == "-":
            result = self.current_value - second_value
        elif self.current_operator == "*":
            result = self.current_value * second_value
        elif self.current_operator == "/":
            # Handle division safely
            if second_value == 0: # So that we cant divide by 0 (i got this idea from AI)
                result = "Error"  # displays "Error" for division by zero
            else:
                result = self.current_value // second_value  # Use integer division
        else:
            result = self.label["text"]  # If no valid operator keep the same value

        self.label.config(text=str(result))  # Display the result
        self.current_operator = None  # Clear the operator so that you can add something new to your answer
        self.is_new_entry = True  # Ready for the next input

    # Clear the display and reset the calculator state
    def clear(self):
        self.label.config(text="0")
        self.current_value = 0
        self.current_operator = None
        self.is_new_entry = True

    # Run the calculator application
    def run(self):
        self.window.mainloop()#what actually runs our window in tkinter



calc = Calculator()
calc.run()
