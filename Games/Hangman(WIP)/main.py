# Import Statements
from random import randint


# Randomly chooses word length based on weighted frequencies
def choose_word():
    random_num = randint(1, 232400)
    if random_num < 50:
        return 1
    elif random_num < 150:
        return 2
    elif random_num < 1150:
        return 3
    elif random_num < 6450:
        return 4
    elif random_num < 16450:
        return 5
    elif random_num < 16450:
        return 6
    elif random_num < 33950:
        return 7
    elif random_num < 57450:
        return 8
    elif random_num < 87450:
        return 9
    elif random_num < 119450:
        return 10
    elif random_num < 150150:
        return 11
    elif random_num < 175650:
        return 12
    elif random_num < 195650:
        return 13
    elif random_num < 210650:
        return 14
    elif random_num < 220650:
        return 15
    elif random_num < 226650:
        return 16
    elif random_num < 229950:
        return 17
    elif random_num < 231450:
        return 18
    elif random_num < 231950:
        return 19
    elif random_num < 232200:
        return 20
    else:
        return 21


# Chooses a random word length
word_length = choose_word()
# Makes an underscore version of the word to display
underscore_word = []
for i in range(0, word_length):
    underscore_word.append("_")

# Prints out an ASCII art for the gallows and the game
print("_________")
print("| /       |")
print("|/")
print("|")
print("|")
print("|")
print("|")
print("|___________\n\n")
print("Here is your word, do your best to guess what it is")
print(*underscore_word, sep="")

