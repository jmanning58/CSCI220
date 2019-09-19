# Calculating the output of Root-Mean-Square (RMS) Average and the Harmonic Mean
# Jacob Manning

#Specifications:
    # Need to get from the user:
        # how many numbers are being used
        # input ea/ number when asked for 
    # Compute mean
    # Compute RMS
    # Compute Harmonic Mean
    # Outputs:
        # RMS
        # Harmonic Mean

# Design:
    # Ask user for: "how_many"
    # "totalrms" -> variable that will change with the RMS
    # "totalHM" -> variable that well change with the Harmonic Mean
    # Ask user for: "numbers"
    # Each value will be squared and added in "totalrms"
    # Each value will be 1/"numbers" and added in "totalHM"
    # Compute mean ->  "totalrms"/"how_many"
    # Compute RMS -> "totalHM" ** 0.5
    # Compute Harmonic Mean -> "(how_many/(1/totalHM))"
    # Print RMS and Harmonic Mean

def RMS_and_HM():

    # Asking for the amount of numbers
    how_many = eval(input("How many numbers are you using: "))

    # Storage variables
    totalrms = 0
    totalHM = 0

    for i in range(how_many):

        # Asking for each number, then store them
        numbers = eval(input("Input a number, then hit <Enter>: "))
        totalrms = totalrms + (numbers**2)
        totalHM = totalHM + (1/numbers)

    # Mean Calculations
    mean = totalrms/how_many
    RMS = round(mean**.5, 3)
    HM = (how_many/totalHM)

    # Outputs for the user
    print("RMS Average: ", RMS)
    print("Harmonic Mean: ", HM)

RMS_and_HM()