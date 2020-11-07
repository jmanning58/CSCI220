# This program will run a Tic-Tac-Toe game for 2 users
#Jacob Mannning

# Specifications:
    # Print a 'board' in command line
    # Request input from users
    # Check for correct inputs
    # Change correct locations for each user
    # Print board with every alteration
    # Show results of game depending on who won or tied

# Design:
    
        # build_board Function:

            # Creates a list of numbers for the board
            # Only returns the list

        # board_display Function(takes in 'build_board'):

            # Assign each number to a spot
            # Print each line with spot and '|' for space

        # fill_spot Function(takes in 'build_board', chosen spot, and which player):

            # Change spot to 'int' for internal use
            # If statement to change 'x' and insert 'X' it if so
            # Else statement to change 'y' and insert 'O' if so

        # legit_spot Function(takes in 'build_board' and chosen spot):

            # Convert spot to 'int' for internal use
            # If statement for if spot is between 0 and 10:

                # If the spot is the return True
                # Else request the user pick somewhere else and return False
            
            # Else statement for the nonexisting spot that returns False

        # game_won Function(takes in 'build_board'):

            # If statement checking from the top right corner's possibilities:
                
                # Checks first row and column for possibilities, return True if so

            # If statement checking from the center possibility:

                # Checks for diagonal possibilities
                # Checks for middle column possibility
                # Checks for middle row possibility
                # Return True if so

            # If statement checking from the bottow left corner's possibilities:

                # Checks last column and bottom row for possiblities, return True if so

            # Else statement for if none of the possiblities are valid, return False

        # game_over Function(takes in 'game_won'):

            # Calls 'game_won' to check if game is over
            # If statement to end game is there is a winner
            # Elif statement to check if there are remaining possibilities
            # Return None to state that the game is not over
    
        # tic_tac_toe Function:
            
            # Calling the number list and displaying it with the board
            # For loop that will run for amount of turns to end game:

                # While loop to make sure player 1 inputs a correct response
                # When while is broken call 'fill_spot' to add player 1's value
                # Reprint board and check to see if there is a winner
                # If statements to end game if there is a winner or tied
                # Repeat the last 4 lines for player 2

        # main Function:

            # Tests are ran here
            # play_game is only function called

# Creates a list of numbers 
def build_board():

    number_list = [1,2,3,4,5,6,7,8,9]

    return number_list
    
# Creates a board for user to see in command line (Void)
def board_display(board_spots):

    # Gather the spots on the board
    p1 = board_spots[0]
    p2 = board_spots[1]
    p3 = board_spots[2]
    p4 = board_spots[3]
    p5 = board_spots[4]
    p6 = board_spots[5]
    p7 = board_spots[6]
    p8 = board_spots[7]
    p9 = board_spots[8]

    # Have them display
    line1 = print( p1, "|", p2, "|", p3)
    line2 = print("-----------")
    line3 = print( p4, "|", p5, "|", p6)
    line4 = print("-----------")
    line5 = print( p7, "|", p8, "|", p9)

# Replaces number on board with 'X' or 'O' (Void)
def fill_spot(board, spot, player):

    # Makes the spot into an integer, not a string
    spot = int(spot)
    
    # Changes the spot requested to X
    if player == 'x':
        player = player.upper()
        board.insert(spot, player)
        board.remove(spot)

    # Changes the spot requested to O
    elif player == 'y':
        player = 'O'
        board.insert(spot, player)
        board.remove(spot)

# Checks to make sure the input is 1-9 (Boolean)
def legit_spot(board, spot):

    # Changes spot into integer to be used
    spot = int(spot)
    if 0 < spot < 10:

        # Checks to see if the number typed to also in the list
        if board[spot-1] == spot:
            return True

        # If spot has been used by other player
        else:
            print("That spot is already taken")
            print("Pick somewhere else")
            return False

    # If spot requested is not on the board
    else:
        print("That is not a spot on the board")
        print("Please try again")
        return False
        
# Will check the board to evaluate if game has been won (Boolean)
def game_won(board):

    # Multiple if statements checking possibilities across board
    if board[0] != 1:
        if board[0] == board[1]:
            if board[1] == board[2]:
                return True

        elif board[0] == board[3]:
            if board[3] == board[6]:
                return True
            
    if board[4] != 5:
        if board[4] == board[0]:
            if board[4] == board[8]:
                return True

        if board[4] == board[1]:
            if board[4] == board[7]:
                return True

        if board[4] == board[2]:
            if board[4] == board[6]:
                return True

        elif board[4] == board[3]:
            if board[4] == board[5]:
                return True

    if board[8] != 9:
        if board[8] == board[5]:
            if board[5] == board[2]:
                return True

        elif board[8] == board[7]:
            if board[7] == board[6]:
                return True

    # If we don't have a winner then the game is not won
    return False

# Calls 'game_won' 
def game_over(board):

    # Calling game_won to find if there's a winning set
    winner = game_won(board)
    if winner == True:
        return True
    
    # If no winning set are there any turns left?
    elif winner == False:
        numbers = 0

        while numbers == 0:
            if 1 == board[0]:
                numbers += 1

            if 2 == board[1]:
                numbers += 1

            if 3 == board[2]:
                numbers += 1

            if 4 == board[3]:
                numbers += 1

            if 5 == board[4]:
                numbers += 1

            if 6 == board[5]:
                numbers += 1

            if 7 == board[6]:
                numbers += 1

            if 8 == board[7]:
                numbers += 1

            if 9 == board[8]:
                numbers += 1

            elif numbers == 0:
                return False

    # If moves remain return stating nothing happened here
    return None

# Function that runs the game
def tic_tac_toe():

    # Getting the list and printing it out
    number_list = build_board()
    board_display(number_list)

    # For each loop each player has a turn, and there is only 9 spots, so we need at most 5
    for i in range(5):
        print("Please input a whole number between 1-9")

        # Loop to make the player input a valid number
        while True:
            x_choice = input("Player 1: ")

            # If the spot is a valid location break out of the loop
            if legit_spot(number_list, x_choice):
                break

        # Sending input to change into X and redisplay
        fill_spot(number_list, x_choice, 'x')
        board_display(number_list)

        # Deciding if the game is still going
        winner = game_over(number_list)
        if winner == True:
            print("Player 1 wins!")
            break
        
        if winner == False:
            print("You've tied!!!")
            break

        # Loop to make the player input a valid number
        while True:
            o_choice = input("Player 2: ")

            # If the spot is a valid location break out of the loop
            if legit_spot(number_list, o_choice):
                break

        # Sending input to change into O and redisplay
        fill_spot(number_list, o_choice, 'y')
        board_display(number_list)

        # Deciding if the game is still going
        winner = game_over(number_list)
        if winner == True:
            print("Player 2 wins!")
            break

        if winner == False:
            print("You've tied!!!")
            break

# To play game and run Tests
def main():
    
    # # Test -> Can draw board
    # print("Do values print?")
    # board_display(['X',2,'O',4,5,'K',7,'M',9])

    # # Test -> Fill spot changing positions on board
    # print("Are items in the list replaced?")
    # testlist = [1,2,3,4,5,6]
    # fill_spot(testlist, 5, 'x')
    # print(testlist)

    # # Test -> Can confirm spots exist or if taken request new input
    # print("True if spot isn't taken and requests to pick somewhere else when False?")
    # legit_spot(testlist, 5)
    # print(legit_spot(testlist, 4))

    # # Test -> Returns True if game has been won and False if not
    # print("Has the correct outputs displayed?")
    # someone_won = print(game_won(['x','x','x',4,5,6,7,8,9]))
    # won_game = print(game_won(['x',2,3,'x',5,6,7,'x',9]))
    
    # # Test -> Checking for confirmation game is over
    # print("Is game over with winner True?")
    # print(game_over(['j','j','j',4,5,6,7,8,9]))
    # print("Is game over with Tie = False?")
    # print(game_over(['x','o','x','x','o','o','o','x','x']))
    # print("If moves left Continue = None?")
    # print(game_over([1,2,3,'x','o',6,7,8,9]))

    tic_tac_toe()

main()
