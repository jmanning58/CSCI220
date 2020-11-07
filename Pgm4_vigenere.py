## This program will implement the Vigenere cipher
## Jacob Manning

# Specification:
    # import graphics
    # window size
    # Entry box placements
    # Message box placements
    # Need to get from the user:
        # message to code
        # keyword
    # Change entrys to UPPERCASE
    # Change entrys to have no spaces
    # Encrypt entrys 
    # Compute entrys 
    # Outputs:
        # Encrypted results

# Design: 
    # Create window to work in
        # Title of the window 
        # Size of the window
    # Text to be drawn for user to see:
        # "request1" -> Message to Code
        # "request2" -> Enter Keyword
        # "encode" -> Encode button
    # Ask user for:
        # "message_code" -> entry point for string to be encrypted
        # "keyword_code" -> enty point for string to be encrypted against
        # "button" -> to be clicked to start encryption
    # Retrieve "message" and "keyword"
        # "obtain_message" -> getting the message
        # "altered_message" entry to be UPPERCASE with no spaces
        # "obtain_keyword" -> getting the keyword
        # "altered_keyword" entry to be UPPERCASE with no spaces
    # Run "altered_message" against "altered_keyword"
        # Loop for encryption with the length of altered_message:
            # "message_letter" -> getting the letter from a certain position
            # "encrypt_message" -> changing letter to number then changing it to a number we're familiar with
            # "keyword_letter_pos" -> making sure we're keeping the keyword letter position in sync with the message letter
            # "keyword_letter" -> getting the keyword letter
            # "encrypt_keyword" -> changing that letter to a number and putting it to a number we are familiar with
            # "encrypted_code" - puts the two "encrypt_message" and "encrypt_keyword" together and loop it and put the number back so the machine can read it
            # "new_letter" -> the new character that is created
    # Final Outputs:
        # Delete:
            # "button_base", "button", "request3"
        # "answer" -> the "encrypted_message" results
        
from graphics import *
    

def vigenere():

    # Creating the window
    width = 600
    height = 400
    win = GraphWin("Vigenere", width, height)

    # Creating instructions for the user
    request1 = Text(Point(100,60), "Message to code  ")
    request2 = Text(Point(110,110), "Enter Keyword   ")
    request3 = Text(Point(300, 185), "Encode")
    button_base = Rectangle(Point(260, 160), Point(340,210))
    button = Rectangle(Point(265,165), Point(335, 205))
    
    # Colors for instructions and drawing them
    button_base.setOutline('black')
    button_base.setFill('gray')
    button.setOutline('silver')
    button.setFill('snow')
    request1.draw(win)
    request2.draw(win)
    button_base.draw(win)
    button.draw(win)
    request3.draw(win)

    # Entry boxes ready for input
    message_code = Entry(Point(390, 60), 39)
    message_code.setFill('snow')
    keyword_code = Entry(Point(305, 110), 20)
    keyword_code.setFill('snow')
    message_code.draw(win)
    keyword_code.draw(win)
    win.getMouse()

    # Retrieve inputs
    obtain_message = message_code.getText()
    altered_message = obtain_message.replace(' ', '')
    altered_message = altered_message.upper()
    obtain_keyword = keyword_code.getText()
    altered_keyword = obtain_keyword.replace(' ','')
    altered_keyword = altered_keyword.upper()
    
    # List box of mystery
    mystery_list = []

    # Changing letters to numbers
    for i in range(len(altered_message)):
        message_letter = altered_message[i]
        encrypt_message = ord(message_letter)
        encrypt_message -= 65

        keyword_letter_pos = i % len(altered_keyword)
        keyword_letter = altered_keyword[keyword_letter_pos]
        encrypt_keyword = ord(keyword_letter)
        encrypt_keyword -= 65

        encrypted_code = (encrypt_message + encrypt_keyword) % 26
        encrypted_code += 65
        new_letter = chr(encrypted_code)

        mystery_list.append(new_letter)

    encrypted_message = ''.join(mystery_list)

    # Outputs and window changes
    button_base.undraw()
    button.undraw()
    request3.undraw()
    ansmessage = Text(Point(300,210), "Resulting Message")
    answer = Text(Point(300,230), encrypted_message)
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click Anywhere to Close Window")
    ansmessage.draw(win)
    answer.draw(win)
    instructions.draw(win)

    win.getMouse()
    win.close()

def main():
    vigenere()

main()