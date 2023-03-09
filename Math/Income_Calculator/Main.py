def yes_or_no(question):
    user_input = input(question + " Y/N\n")
    if user_input.lower() == "y":
        return True
    else:
        return False


def one_year_income():
    return custom_time_income(1)


def custom_time_income(years):
    if exponential:
        return round((base_value * (1 + interest) ** (frequency * years)), 2)
    else:
        return round((base_value * (1 + interest * frequency * years)), 2)


base_value = float(input("What is your starting value?\n"))
interest = float(input("How much interest does it earn (write as a percent without the sign)\n")) / 100
frequency = int(input("How many times do you earn that interest in a year\n"))
exponential = yes_or_no("Does your interest earn interest?")
time_input = float(input("For how many years would this be gaining interest? (works with decimals, so .5 would be 6 "
                         "months\n"))
print("In " + str(time_input) + " years, you will have $" + str(custom_time_income(time_input)))
