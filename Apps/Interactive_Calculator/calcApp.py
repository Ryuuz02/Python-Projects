# Import Statements
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


# Require 2.0.0 or after
kivy.require("2.0.0")


# Grid layout display of our calculator, we use 4 columns
class calculator(GridLayout):
    def __init__(self, **kwargs):
        super(calculator, self).__init__(**kwargs)
        self.cols = 4



# Calculator Application
class calcApp(App):
    # When the program is ran
    def build(self):
        # Adds the grid layout
        calc = calculator()
        # Some values to store information
        self.string_total = ""
        self.total1 = ""
        self.operator = ""
        # Adds the arrangement of buttons to match a normal calculator. In total has 0-9, add, subtract, divide,
        # multiply, a negative/positive switch, and the equal sign
        # Also all are in buttons that are tied to an appropriate function
        one_button = Button(text="1", background_color=(0, 0, 1), bold=True)
        one_button.bind(on_release=self.one_pressed, on_press=self.press_down)
        calc.add_widget(one_button)
        two_button = Button(text="2", background_color=(0, 0, 1), bold=True)
        two_button.bind(on_release=self.two_pressed, on_press=self.press_down)
        calc.add_widget(two_button)
        three_button = Button(text="3", background_color=(0, 0, 1), bold=True)
        three_button.bind(on_release=self.three_pressed, on_press=self.press_down)
        calc.add_widget(three_button)
        plus_button = Button(text="+", background_color=(0, 1, 0))
        plus_button.bind(on_release=self.plus_pressed, on_press=self.press_down)
        calc.add_widget(plus_button)
        four_button = Button(text="4", background_color=(0, 0, 1), bold=True)
        four_button.bind(on_release=self.four_pressed, on_press=self.press_down)
        calc.add_widget(four_button)
        five_button = Button(text="5", background_color=(0, 0, 1), bold=True)
        five_button.bind(on_release=self.five_pressed, on_press=self.press_down)
        calc.add_widget(five_button)
        six_button = Button(text="6", background_color=(0, 0, 1), bold=True)
        six_button.bind(on_release=self.six_pressed, on_press=self.press_down)
        calc.add_widget(six_button)
        minus_button = Button(text="-", background_color=(0, 1, 0))
        minus_button.bind(on_release=self.minus_pressed, on_press=self.press_down)
        calc.add_widget(minus_button)
        seven_button = Button(text="7", background_color=(0, 0, 1), bold=True)
        seven_button.bind(on_release=self.seven_pressed, on_press=self.press_down)
        calc.add_widget(seven_button)
        eight_button = Button(text="8", background_color=(0, 0, 1), bold=True)
        eight_button.bind(on_release=self.eight_pressed, on_press=self.press_down)
        calc.add_widget(eight_button)
        nine_button = Button(text="9", background_color=(0, 0, 1), bold=True)
        nine_button.bind(on_release=self.nine_pressed, on_press=self.press_down)
        calc.add_widget(nine_button)
        multiply_button = Button(text="*", background_color=(0, 1, 0))
        multiply_button.bind(on_release=self.multiply_pressed, on_press=self.press_down)
        calc.add_widget(multiply_button)
        negative_button = Button(text="+/-", background_color=(1, 0, 0))
        negative_button.bind(on_release=self.negative_pressed, on_press=self.press_down)
        calc.add_widget(negative_button)
        zero_button = Button(text="0", background_color=(0, 0, 1), bold=True)
        zero_button.bind(on_release=self.zero_pressed, on_press=self.press_down)
        calc.add_widget(zero_button)
        dot_button = Button(text=".", background_color=(1, 0, 0))
        dot_button.bind(on_release=self.dot_pressed, on_press=self.press_down)
        calc.add_widget(dot_button)
        divide_button = Button(text="/", background_color=(0, 1, 0))
        divide_button.bind(on_release=self.divide_pressed, on_press=self.press_down)
        calc.add_widget(divide_button)
        equal_button = Button(text="=", background_color=(1, 1, 1))
        equal_button.bind(on_release=self.equal_pressed)
        calc.add_widget(equal_button)
        return calc

    def press_down(self, obj):
        obj.background_color = (1, 1, 1)

    # Number pressed just adds that number to the running total
    def one_pressed(self, obj):
        self.string_total += "1"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def two_pressed(self, obj):
        self.string_total += "2"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def three_pressed(self, obj):
        self.string_total += "3"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def four_pressed(self, obj):
        self.string_total += "4"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def five_pressed(self, obj):
        self.string_total += "5"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def six_pressed(self, obj):
        self.string_total += "6"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def seven_pressed(self, obj):
        self.string_total += "7"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def eight_pressed(self, obj):
        self.string_total += "8"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def nine_pressed(self, obj):
        self.string_total += "9"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    def zero_pressed(self, obj):
        self.string_total += "0"
        obj.background_color = (0, 0, 1)
        print(self.string_total)

    # Switch between negative/positive
    def negative_pressed(self, obj):
        obj.background_color = (1, 0, 0)
        # If there is nothing there, will add a negative to the beginning
        if len(self.string_total) == 0:
            self.string_total = "-"
        # If there is something
        else:
            # If it is already negative
            if self.string_total[0] == "-":
                # If the only thing is a negative sign
                if len(self.string_total) == 1:
                    # Will bring it back to positive nothing
                    self.string_total = ""
                # Else it will just get rid of the negative
                else:
                    self.string_total = self.string_total[1:]
            # If it is currently positive
            else:
                # Adds a negative
                self.string_total = "-" + self.string_total
        print(self.string_total)

    # Similar to numbers, just adds a decimal (WIP still)
    def dot_pressed(self, obj):
        obj.background_color = (1, 0, 0)
        if "." not in self.string_total:
            self.string_total += "."
        print(self.string_total)

    # The math operators all work the same
    def plus_pressed(self, obj):
        obj.background_color = (0, 1, 0)
        # If the first part of the operation is blank
        if self.total1 == "":
            # Will take the running total as the first part
            self.total1 = self.string_total
            # Resets the string total
            self.string_total = ""
            # Tells the calculator what operator it should use for math
            self.operator = "+"

    def minus_pressed(self, obj):
        obj.background_color = (0, 1, 0)
        if self.total1 == "":
            self.total1 = self.string_total
            self.string_total = ""
            self.operator = "-"

    def divide_pressed(self, obj):
        obj.background_color = (0, 1, 0)
        if self.total1 == "":
            self.total1 = self.string_total
            self.string_total = ""
            self.operator = "/"

    def multiply_pressed(self, obj):
        obj.background_color = (0, 1, 0)
        if self.total1 == "":
            self.total1 = self.string_total
            self.string_total = ""
            self.operator = "*"

    # Equal sign function
    def equal_pressed(self, obj):
        # If the first value is not empty
        if self.total1 != "":
            # If the second part is empty
            if self.string_total == "":
                # Will just return the first value
                print(self.total1)
            # If there is a second value
            else:
                # Prints the mathematical evaluation of it
                print(eval(self.total1 + self.operator + self.string_total))
                # Resets the string total
                self.string_total = ""
            # Resets the first value total
            self.total1 = ""
        # If there is not a proper value for the first total
        else:
            print("There was not a first value")


calcApp().run()
