# Import Statements
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

# Check to make sure up to date
kivy.require("2.0.0")

# Using the builder to modify the screens
Builder.load_string("""
# Home screen layout
<HomeScreen>:
    # Grid layout of 2 columns
    GridLayout:
        cols: 2
        Button:
            # Button to go to the login screen
            text: "Login Here"
            on_press: root.manager.current = "Login"
        Button:
            # Button to go to the registration screen
            text: "Register Here"
            on_press: root.manager.current = "Register"
<LoginScreen>:
    # Also 2 column grid
    GridLayout:
        cols: 2
        Label:
            # Prompt for username
            text: "Enter Username"
        TextInput:
            # Takes in the user's username, when they press enter, it will take anything they've typed and find that 
            # string in the txt file
            hint_text: "Enter Username Here"
            multiline: False
            on_text_validate: root.find_username(self.text)
        Label:
            # Prompt for password
            text: "Enter Password"
        TextInput:
            # Takes in the user's password, when they press enter, it will take anything they've typed and find that 
            # string in the txt file
            hint_text: "Enter Password Here"
            multiline: False
            on_text_validate: root.find_password(self.text)
        Button:
            # Button to return to home screen
            text: "Return To Home Screen"
            on_press: root.manager.current = "Home"
        Button:
            # Button to go to register screen
            text: "Register Here"
            on_press: root.manager.current = "Register"
<RegisterScreen>:
    GridLayout:
        cols: 2
        Label:
            # Prompt for username
            text: "Register Username"
        TextInput:
            # Takes in the user's username, when they press enter, it will take anything they've typed and add that 
            # string
            hint_text: "Enter Username Here"
            multiline: False
            on_text_validate: root.add_username(self.text)
        Label:
            # Prompt for password
            text: "Register Password"
        TextInput:
            # Takes in the user's password, when they press enter, it will take anything they've typed and add that 
            # string
            hint_text: "Enter Password Here"
            multiline: False
            on_text_validate: root.add_password(self.text)
        Button:
            # Button to go back to home screen
            text: "Return To Home Screen"
            on_press: root.manager.current = "Home"
        Button:
            # Button to go back to login screen
            text: "Login Here"
            on_press: root.manager.current = "Login"
# Screen for once you've logged in
<LoggedInScreen>:
    # Grid layout of 2 columns
    GridLayout:
        cols: 2
        Label:
            # Label saying they logged in
            text: "Congratulations, You've Logged In"
        Button:
            # Button to go back to home screen
            text: "Logout"
            on_press: root.manager.current = "Home"

""")


# Searches the file for the input string if it exists
def search_file(searched_text, login_type):
    # Finds the spot
    spot = find_position(searched_text, login_type)
    # If it was not found
    if spot == -1:
        return False
    # If it was found
    else:
        return True


# Finds the exact position of a string if it exists
def find_position(searched_text, login_type):
    # With the file open as f
    with open("login_info.txt", "r") as f:
        # Finds the file length to iterate through
        with open("login_info.txt", "r") as g:
            file_length = len(g.read())
            g.seek(0)
            file_length += (len(g.readlines()) - 1)
        # Prepares variable for loop
        found = False
        spot = 0
        # While it is not found
        while not found:
            # Takes the next line
            next_line = f.readline()
            # Checks to see if it is password or username
            if next_line[0:8] == login_type:
                # If its the correct type, finds the personal info
                iterated_name = next_line[9:len(next_line) - 1]
                # If it matches the user input
                if searched_text.lower() == iterated_name.lower():
                    # Returns that it is found
                    found = True
            # If it has hit the end without finding it
            if f.tell() == file_length and not found:
                spot = -1
                break
            # If it is not found
            if not found:
                # Increments the spot
                spot += 1
        # Returns the spot it was found (or -1 if it was not)
        return spot


# Home screen class
class HomeScreen(Screen):
    pass


# Screen for logging in
class LoginScreen(Screen):
    def __init__(self, name):
        # Variables we can use to store info
        super(LoginScreen, self).__init__(name=name)
        self.username_position = -1
        self.logged_password = False

    # function for buttons to use to find inputed username
    def find_username(self, obj):
        # Tests if the username is in the file
        found = search_file(obj, "username")
        # If it is
        if found:
            # Tells the user and stores the location
            print("Found your Username")
            self.username_position = find_position(obj, "username")
        else:
            # Says it was not found
            print("Invalid Username")

    # Function for buttons to use to find the inputed password
    def find_password(self, obj):
        # If there was no username put in, tells the user
        if self.username_position == -1:
            print("Please put in a username first")
        else:
            # With the file open as f
            with open("login_info.txt", "r") as f:
                # Reads the entire file to str_lst
                str_lst = f.readlines()
                # The correct password is the one after the username in the file
                password = str_lst[self.username_position + 1]
                # Test if the password is the last thing in the list
                if (self.username_position + 2) == len(str_lst):
                    # If it is, there is no /n at the end, so we don't need to cut it off with - 1
                    if obj == password[9:len(password)]:
                        # Tells the user their password was found and brings them to the logged in screen
                        print("Found Password")
                        self.logged_password = True
                        self.parent.current = "Logged"
                    else:
                        # Otherwise, tells the user it was wrong
                        print("Incorrect Password")
                # If it is not the last line in the file, we need - 1 to cut off the \n at the end
                elif obj == password[9:len(password) - 1]:
                    # Tells the user it was found and brings them to the logged in screen
                    print("Found Password")
                    self.logged_password = True
                    self.parent.current = "Logged"
                else:
                    # Else, tells the user it was wrong
                    print("Incorrect Password")


# Screen for registering new info
class RegisterScreen(Screen):
    # Function for adding username
    def add_username(self, obj):
        # With the file open as f
        with open("login_info.txt", "a+") as f:
            # Goes to the beginning of the file
            f.seek(0)
            # If there is nothing currently in the file, adds it automatically
            if len(f.read()) == 0:
                f.write("username:" + obj)
            # Else, it will check the entire file to see if there is already a user with that username
            else:
                f.seek(0)
                found = search_file(obj, "username")
                # If there isn't adds, the username
                if not found:
                    f.write("\nusername:" + obj)
                # If there is, will tell the user it is already in use
                else:
                    print("That username is already in use")

    # Function for adding password
    def add_password(self, obj):
        # No checks needed for the password since we don't have any restrictions yet, might be something to add
        with open("login_info.txt", "a+") as f:
            f.write("\npassword:" + obj)


# Screen for once you've logged in
class LoggedInScreen(Screen):
    pass


# Application for the entire thing
class LoginApp(App):
    # When the code is ran
    def build(self):
        # Creates a screen manager
        sm = ScreenManager()
        # Adds all the screens and their appropriate name
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(RegisterScreen(name="Register"))
        sm.add_widget(LoggedInScreen(name="Logged"))
        # Returns the screen manager
        return sm


# Assigns the app to a variable and runs it
loginapp = LoginApp()
loginapp.run()
