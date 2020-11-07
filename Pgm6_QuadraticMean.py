# This program will take a text file, read it, pull the lines of numbers, and run them through 4 functions to compute the quadratic mean
# Jacob Manning

# Specifications:
    # Take in a text file containing lines of numbers
    # Quadratic_mean function reads the file out gives outputs
    # Send each line to to_numbers function to convert to a list of numbers
    # Send the numbers to make_squares function to modify the list to square each value
    # Send the new list to sum_list for the total values to be computed
    # Send both the total value and how many terms to compute_mean function to compute the quadratic mean
    # Outputs:
        # Terms being processed
        # Quadratic Mean

# Design:

    # quadratic_mean Function:
        # Input a .txt file
        # Read file text stored in 'base_numbers'
        # Send read text (base_numbers) to to_numbers function
        # Send list from 'number_list' to make_squares function
        # Send list from 'squared_numbers to sum_list function
        # For loop(number of lines):
            # 'Amount' -> number of terms in each line
            # 'Line_totals' -> Gets each lines sum
            # Send 'line_totals' and 'amount' to compute_mean function
        # Output:
            # Print the line being computed with 'found_mean'

    # to_numbers Function(takes 1 argument):
        # First list -> storage for lines to start
        # For loop(running off of function argument):
            # storing each read line as list in First list
        # Second list -> storage for values that are floats
        # For loop(running off of length of First list):
            # taking each list and removing the \n
            # 'new_values' -> splitting the values into single value lists
            # Third list -> resets to empty list with each iteration
            # For loop(running off of length of 'new_values'):
                # change the contents of each single value into a float
                # add 'numbers' to Third list
            # Add Third list to Second list
        # Return Second list

    # make_squares Function(takes 1 argument):
        # First list -> empty for storage of final values
        # For loop(running off of each line in the list):
            # Second list -> resets with every iteration
            # For loop(running every off of each item in the list):
                # number -> square item
                # add to Second list
            # Add Second list to First list
        # Return the First list

    # sum_list Function(takes 1 argument):
        # First list -> Empty for totals to be stored
        # For loop(running off of the lines in the list):
            # 'value' -> to be reset to zero with every iteration
            # For loop( running off of each number in the line):
                # adding the numbers together
        # Put each lines sum into First list 
        # Return the totals
    
    # compute_mean Function(takes 2 arguments):
        # Take the first argument and divide it by the second
        # Put the value to the power of .5 (**.5)(square root)
        # Return the quadratic mean

    # main Function
        # only call the quadratic_mean


# Function that only computes logic of program
def quadratic_mean():

    # Opening the text file, getting the contents(as a string), and closing the file
    with open ("C:/Users/vampi/Desktop/SchoolPapers/220/squares.txt", "rt") as base_numbers:

    # Sending the contents to be calculated 
        number_list = to_numbers(base_numbers)
        squared_numbers = make_squares(number_list)
        sum_of_values = sum_list(squared_numbers)

        # For loop that runs off the length of how many lines
        for i in range(len(sum_of_values)):
            # Get amount of terms being used in each line and totals
            amount = len(number_list[i])
            line_totals = sum_of_values[i]
            quad_mean = compute_mean(line_totals, amount)

            # The output of all your hard work
            print(number_list[i], ' = ', quad_mean)

# Function that converts contents from a string to a list
def to_numbers(string):

    # Empty variable for initial storage as list
    lines = []
    
    # For loop for seperating the lines and storing them
    for the_line in string:

        lines.append(the_line)

    # Empty variable for values ready to be returned
    new_lines = []

    # For loop that removes \n from the end of each line
    for i in range(len(lines)):
        values = lines[i]
        line_removal = values[:-1]
        new_values = line_removal.split(',')

        sub_new_lines = []

        # For loop that changes the values to floats
        for j in range(len(new_values)):
            numbers = float(new_values[j])
            sub_new_lines.append(numbers)

        new_lines.append(sub_new_lines)

    # Return the new found list
    return new_lines

# Function that takes the list and sqares each number
def make_squares(lists):

    # Empty variable for storage as list
    number_list = []

    # For loop for splitting the string to create a list of strings
    for line in lists:
        # List that will be reset with each line
        sub_number_list = []

        # For loop that squares each value
        for spot_value in line:
            number = spot_value**2
            sub_number_list.append(number)

        number_list.append(sub_number_list)

    # Return the new found list
    return number_list

# Function that takes your squared numbers and adds them together
def sum_list(lists):

    # Empty variable for storage
    totals = []

    # For loop that adds the sum value to the total list
    for line in lists:
        value = 0

        # For loop thats sums each line
        for spot in line:
            value += spot

        totals.append(value)

    # Return the total amount
    return totals

# Function that computes your quadratic mean
def compute_mean(sum, n):

    the_mean = (sum/n)**.5

    # Returning the quadratic mean
    return the_mean

# Function that calls only your quadratic_mean function
def main():
    quadratic_mean()

main()