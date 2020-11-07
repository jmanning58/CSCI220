# This program will allow multiple users to play Hangman off of a text file
# Jacob Manning

# Specifications:
    # Import Graphics
    # Display starting in graphic window
    # Read random word from imported text file
    # Blanks for letter to guess
    # Fill blanks if guess is correct, store in window if not
    # Input box for user to input guess
    # Number showing how many turns left, changes based on the word
    # Play again and quit button
    # Create objects for the Hangman, 7 parts to it

# Design:

    # random_words Function:

        # Opens and reads a file
        # Creates a list with the words from the file
        # Closes the file
        # Only returns the list

    # random_pick Function(takes in 'word_list'):

        # Randomly picks an integer between 0 - 9
        # Only returns the word from the numbered spot

    # word_spaces Function(takes in 'secret_word'):

        # Creates a list blank spaces to be stored
        # For loop to append spaces based on length of word
        # Only returns the list

    # correct_letter Function(takes in 'secret_word' and 'guessed_letter'):

        # For loop checking each letter in the 'secret_word' for 'guessed_letter' compatibility
            # Returns True if there is compatibility
        # Returns False if letter doesn't exist

    # letter_replacment Function(takes in 'spaces', 'secret_word', and 'guessed_letter'):

        # For loop inserting 'guessed_letter' in the correct spot
            # Also removes the '_' left behind

    # game_won Function(takes in 'spaces'):

        # For loop that runs for the length of 'spaces'
            # If a '_' is found then return False
        # Will return True if there are no '_' found

    # play_again Function:

        # Ask the user if they would like to play again
        # Alter letter in case it is not entered as uppercase
        # If 'Y' then call 'main', if 'N' return to end program

    # hangman Function:
        
        # Calling the file and displaying the spaces
        # While loop running off of the amount of guesses left:

            # Request input from user for their guess
            # If loop checking guess, and replacing if correct
            # Checking if game has been won
            # If guess was incorrect minus a guess

    # window Function:

        # Creates window with title and size
    
    # letters_box Function(takes in 'window'):

        # Creates a box in the window filled with letters from A - Z

    # guessed_box Function(takes in 'window' and ?):

        # Creates a box in the window
        # Fills with the invalid letters 

    # users_box Function(takes in 'window'):

        # Creates a text box for the user to type in their guess

    # platform Function(takes in 'window'):

        # Creates the stage for the hangman


# Notes:
    # Consider having a small window in upper corner with letters available
    # Window below it for used invalid letters
    # Hint feature to give a one word answer stating the genre of the word

from graphics import *
from random import *

# Function that converts contents of file to list
def random_words():

    # Opens and closes file
    with open ("wordlist.txt", "rt") as word_list:

        original_words = []
        usable_words = []

        # Pulls each word and stores in the above list
        for each_word in word_list:
            original_words.append(each_word)

        # For loop that removes \n from the end of each line
        for i in range(len(original_words)):
            pulled_word = original_words[i]
            extra_removal = pulled_word[:-1]
            usable_words.append(extra_removal)

    return usable_words

# Selects a random word to return
def random_pick(word_list):

    secret_pick = randint(0,9)

    return word_list[secret_pick]

# Generates '_' for each letter and prints new '_' for correct guesses
def word_spaces(secret_word):

    spaces = []

    # Length of word for blanks
    for i in range(len(secret_word)):
        space = '_ '
        spaces.append(space)

    return spaces

# Checking to see the letter guessed is in the word (Boolean)
def correct_letter(secret_word, guessed_letter):

    # For loop checking each letter for guess
    for i in range(len(secret_word)):
        if guessed_letter == secret_word[i]:
            return True
        
    return False

# Replaces '_' with guessed_letter
def letter_replacment(spaces, secret_word, guessed_letter):

    # For loop inserting correct letters
    for i in range(len(secret_word)):
        if guessed_letter == secret_word[i]:
            spaces.insert(i, guessed_letter)
            spaces.pop(i+1)

# To check if all spaces are full (Boolean)
def game_won(spaces):

    # For loop that returns False if a '_' is found
    for i in range(len(spaces)):
        if spaces[i] == '_ ':
            return False

    return True

# Set to rerun the program again if user wants
def play_again():

    restart = input("Would You Like To Play Again? Y/N ")
    if restart.upper() == 'Y':
        main()

    elif restart.upper() == 'N':
        return

# For playing the game
def hangman():

    words = random_words()
    secret_word = random_pick(words)
    spaces = word_spaces(secret_word)
    # win = window()

    guesses = 7
    # Runs til guesses run out
    while guesses >= 1:
        # guess_box(win)

        print("Guesses: ", guesses)
        print("Guess a letter")
        print(' '.join(spaces))

        # Requesting input from user 
        guessed_letter = input("Guess: ")

        # If letter if correct: replace and check if game is over
        if correct_letter(secret_word, guessed_letter):
            letter_replacment(spaces, secret_word, guessed_letter)

            winner = game_won(spaces)

            if winner:
                print(' '.join(spaces))
                print("You've won!!!")
                break

        else:
            guesses -= 1
    
    play_again()

# Graphics window for user to interact with
def window():

    width = 800
    height = 800
    win = GraphWin("Hang Man", width, height)

    return win

# Bases of all buttons
def draw_buttons(window):

    # Shape and color of the base of the button with text
    yes_button_base = Rectangle(Point(50, 660), Point(250, 760))
    yes_button_base.setOutline('black')
    yes_button_base.setFill('dark gray')
    yes_button_base.draw(window)

    # Shape and color of the base of the button with text
    no_button_base = Rectangle(Point(300, 660), Point(500, 760))
    no_button_base.setOutline('black')
    no_button_base.setFill('dark gray')
    no_button_base.draw(window)

    # Shape of the top of the button
    yes_button = Rectangle(Point(60, 670), Point(240, 750))
    yes_button.setOutline('dim gray')
    yes_button.setWidth(4)
    yes_button.setFill('snow')
    yes_button.draw(window)

    # Text that is displayed
    yes_request = Text(Point(150, 710), "Yes")
    yes_request.setSize(20)
    yes_request.draw(window)

    # Shape of the top of the button
    no_button = Rectangle(Point(310, 670), Point(490, 750))
    no_button.setOutline('dim grey')
    no_button.setWidth(4)
    no_button.setFill('snow')
    no_button.draw(window)

    # Text that is displayed
    no_request = Text(Point(400, 710), "No")
    no_request.setSize(20)
    no_request.draw(window)

# To make sure mouse click is within button
def was_clicked(pt, rect):

    # To check if there was a click, if not do nothing
    if pt == None:
        return False

    # Button's parameters
    x1 = rect.getP1().getX()
    x2 = rect.getP2().getX()

    y1 = rect.getP1().getY()
    y2 = rect.getP2().getY()

    # Cooridinates of mouse click
    px = pt.getX()
    py = pt.getY()

    # Only will return confirmation if both values are True
    return x1 < px < x2 and y1 < py < y2

# Input box for window
def guess_box(window):

    request = Text(Point(100,60), "What's Your Guess:  ")
    guess = Entry(Point(390, 60), 39)
    guess.setFill('snow')
    guess.draw(window)
    request.draw(window)
    window.getMouse()

# Showing guessed letters
def guessed_box(window, guessed):

    used = Rectangle(Point(50, 50), Point(120, 120))
    used.setOutline('black')
    used.draw(window)

    guesses = Text(Point(55,60), guessed)
    guesses.setSize(20)
    guesses.draw(window)

def main():

    hangman()

main()