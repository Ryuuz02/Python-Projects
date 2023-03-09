# Function for adding a potentially infinite amount of numbers
def add_nums():
    total = 0
    # Takes in user input for how many total numbers to add
    num_of_nums = int(input("How many numbers would you like to add up\n"))
    # For each number they wish to add
    for i in range(0, num_of_nums):
        # Takes in the user input for the number and adds it to the total
        total += float(input("Please type your number below\n"))
    return total


# Just a one size fits all function for math equations
def evaluate_expression(num1, exp, num2):
    if exp == "x" or exp == "*":
        return num1 * num2
    elif exp == "+":
        return num1 + num2
    elif exp == "-":
        return num1 - num2
    elif exp == "/":
        return num1 / num2
    elif exp == "^":
        return num1 ** num2


# Function to subtract infinite amount of numbers
def subtract_nums():
    total = 0
    # User input for how many numbers to subtract
    num_of_nums = int(input("How many numbers would you like to total\n"))
    for i in range(0, num_of_nums):
        # Puts the first input as the number that will be subtracted from
        if i == 0:
            total = float(input("What is your starting value?\n"))
        # Everything after subtracts from that
        else:
            total -= float(input("What number would you like to subtract it by?\n"))
    return total


# Function to multiply any amount of numbers
def multiply_nums():
    total = 0
    # Input for how many numbers to multiply
    num_of_nums = int(input("How many numbers would you like to multiply\n"))
    for i in range(0, num_of_nums):
        if i == 0:
            # First one is the new total value
            total = float(input("Please type your number below\n"))
        else:
            # Everything after just multiplies
            total *= float(input("Please type your number below\n"))
    return total


# Function to divide two user inputed numbers
def divide_nums():
    # First number is the dividend
    dividend_num = float(input("What number would you like to divide\n"))
    # Second number is the divisor
    divisor_num = float(input("What would you like to divide it by?\n"))
    return dividend_num / divisor_num


# Function to run through each operator in the function_lst, the reason this is done separately is because certain
# operators have the same priority (multiply and divide, add and subtract) so we need to keep them together in order
# to properly follow PEMDAS
def symbol_loop(symbol_lst):
    global functions_remaining
    # while loop to check if there are the operators still inside the function_lst
    while any(elem in symbol_lst for elem in function_lst):
        # for each function in the list
        for i in range(0, len(function_lst)):
            i -= counter
            # goes through each type of function from left to right of function_lst
            for j in range(0, len(symbol_lst)):
                symbol_if_loop(symbol_lst[j], i)


# Function to actually do the math and replace values
def symbol_if_loop(symbol, i):
    global functions_remaining
    global counter
    # If there are functions left, and one of the operators still in the equation
    if functions_remaining and equation_split[function_index_list[i]] == symbol:
        # It will find the value of the two numbers
        value = evaluate_expression(float(equation_split[function_index_list[i] - 1]), symbol,
                                    float(equation_split[function_index_list[i] + 1]))
        # Replace the value with where it is supposed to be in equation_split
        equation_split[function_index_list[i]] = value
        # Then get rid of the two values that created this number
        # For example, if the equation is 5 + 5, it would replace the + with 10, then get rid of the two 5's, leaving
        # just 10
        equation_split.pop(function_index_list[i] + 1)
        equation_split.pop(function_index_list[i] - 1)
        # Then removes the iterated operator from function_lst
        function_lst.remove(symbol)
        # Increments the counter so we don't get a keyError
        counter += 1
        # Moves over functions in the function_index_list so that their index values are still correct
        for j in range(0, len(function_index_list)):
            if function_index_list[j] > function_index_list[i]:
                function_index_list[j] -= 2
        # Then, gets rid of the iterated operator's stored index
        function_index_list.pop(i)
        # If the function_lst is empty, stops trying to solve for the equation
        if len(function_index_list) == 0:
            functions_remaining = False


# This function just resets every variable back to starting values
def reset_equation_variables():
    global function_index_list
    global function_lst
    global functions_remaining
    global counter
    counter = 0
    function_index_list = []
    function_lst = []
    functions_remaining = True


# Function that runs when asked to input an eqation
def evaluate_equation(equation_input):
    global equation_split
    global function_index_list
    global function_lst
    global functions_remaining
    global counter
    # Reset the variables back to defaults
    reset_equation_variables()
    # Splits the equation into pieces by spaces
    equation_split = equation_input.split()
    # for each operator in the equation_split
    for i in range(0, len(equation_split)):
        if equation_split[i] in math_functions:
            # Adds the index tied to that operator to function_index_lst
            function_index_list.append(i)
            # And it appends that operator to the function_lst
            function_lst.append(equation_split[i])
    # Goes through every operator and performs their operation
    symbol_loop(["^"])
    counter = 0
    symbol_loop(["*", "x", "/"])
    counter = 0
    symbol_loop(["-", "+"])
    # Prints the end equation
    print(equation_split)


# Assigning variables their default values
equation_split = []
function_index_list = []
function_lst = []
functions_remaining = True
counter = 0
# math_functions is just a list of the operators to iterate through
math_functions = ["x", "*", "-", "+", "/", "^", "(", ")"]
# function_choice is the user input of what to do with the program
function_choice = input("Would you like to:"
                        "\n 1: Add multiple numbers"
                        "\n 2: Subtract multiple numbers"
                        "\n 3: Multiply multiple numbers"
                        "\n 4: Divide two numbers"
                        "\n 5: Input an entire equation\n")
# 1 is add
if function_choice == "1":
    print(add_nums())
# 2 is subtract
elif function_choice == "2":
    print(subtract_nums())
# 3 is multiply
elif function_choice == "3":
    print(multiply_nums())
# 4 is divide
elif function_choice == "4":
    print(divide_nums())
# and 5 is the equation input
elif function_choice == "5":
    evaluate_equation(input("Please type out your equation (This is a WIP, so currently it can only do -, +, x"
                            ", *, /, and ^ operations. Also you must put a space in between, for example '4 + 5')\n"))
