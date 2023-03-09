# Import Libraries
from random import randint
import enchant
from PyDictionary import PyDictionary


# Picks a word length and returns it, picked randomly, weighted by the number of each length of word in the english
# language
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


# Checks if an input word is actually a word
def check_word_validity(input_word):
    checked = d.check(input_word)
    # If it is not, returns false
    if not checked:
        return False
    # If it is, it checks the second dictionary to ensure it has a proper definition
    word_validity = find_word_meaning(input_word)
    # Returns false if it is not recognized, else it returns the value of the check normally
    if word_validity is None:
        return False
    else:
        return checked


# Running is used to control while loop
running = True
# d is the english word dictionary, used only for spellchecking if something is actually a word
d = enchant.Dict("en_US")
# the PyDictionary is for checking meaning and the part of speech
english_dictionary = PyDictionary()
# list of english letters for making words
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]


# Function that finds the meaning of a word, ignores errors so that it isn't constantly printing out lines of errors
def find_word_meaning(input_word):
    return english_dictionary.meaning(input_word, disable_errors=True)


# checks if the input word is actually the part of speech it needs to be
def check_word_type_validity(input_word, word_type):
    # Tries to find the specified part of speech meaning, if it can, returns true
    try:
        english_dictionary.meaning(input_word)[word_type]
        return True
    # If it can't returns false
    except KeyError:
        return False


# Function to create a word with a random length
def create_word_random_length():
    # Checker to see if a word is actually a word
    bad_word = True
    # word string to store the creation
    word = ""
    # Picks a random length for the word
    word_length = choose_word()
    # While it is not a correct word, will run through loop
    while bad_word:
        for j in range(0, word_length):
            # Adds a letter to the word variable for each letter there is supposed to be
            word += alphabet_list[randint(0, 25)]
        # If valid, will stop iterating through loop
        if check_word_validity(word):
            bad_word = False
        # Else it will keep going again
        else:
            word = ""
            word_length = choose_word()
    # When it finds a valid word, returns it
    return word


# Uses the above function to create a specific part of speech word
def create_word_random_length_specific_type(word_type):
    # Creates a valid word
    word = create_word_random_length()
    # Checks if its the right part of speech, returns it if it is
    if check_word_type_validity(word, word_type):
        return word
    # Else, tries again
    else:
        return create_word_random_length_specific_type(word_type)


#  Creates a random grammatically sentence structure given a desired length
def create_random_sentence_structure(sentence_length):
    # You cannot make a 1 word sentence
    if sentence_length == 1:
        return False
    # 2 words can only be noun verb (assuming no implied subject)
    elif sentence_length == 2:
        return ["Noun", "Verb"]
    # 3 different variations of 3 word sentences
    elif sentence_length == 3:
        variation = randint(1, 3)
        if variation == 1:
            return ["Noun", "Verb", "Noun"]
        elif variation == 2:
            return ["Adjective", "Noun", "Verb"]
        else:
            return ["Noun", "Adverb", "Verb"]


# main while loop
while running:
    # User inputs how long of a sentence they want
    user_length = input("How long would you like your sentence? (can go up to 3 words currently), or type 'e' to exit\n"
                        )
    # If they want to exit
    if user_length == "e":
        running = False
    # else makes their input into an integer
    else:
        user_length = int(user_length)
    # creates a sentence structure
    sentence_structure = create_random_sentence_structure(user_length)
    # checks if its not 1 word sentence
    if not sentence_structure:
        print("You cannot create a sentence of that length")
    else:
        # creates a blank list to store our sentence
        sentence = []
        for i in range(0, user_length):
            # For each word there is supposed to be, finds a word that matches the part of speech required
            sentence.append(create_word_random_length_specific_type(sentence_structure[i]))
        # Stops iterating
        running = False
print("Your randomly generated sentence is: ")
# Prints out the sentence as a big string
print(*sentence)
