# Calculating Interest for Payments and Final Amount Paid
# Jacob Manning

# Specifications:
    # Need to get:
        # the "principal" from the user
        # the number of "months" it will take to pay off from the user
        # the "interest" (in percent without symbol) from the user
    # Compute the Rate of Interest
    # Compute the Monthly Payment
    # Compute the Total Amount Paid
    # Compute the Total Amount of Interest Paid
    # Return these to the user:
        # Monthly Payment
        # Total Amount Paid
        # Total Interest Paid

# Design:
    # Ask user for:
        # "interest"
        # "principal"
        # "months"    
    # Compute Rate as -> "interest"/1200
    # Compute Monthly Payments -> (principal * rate * (1 + rate)**months) / (((1 + rate)**months)-1)
    # Compute Total Amount Paid -> Monthly Payments * Months
    # Compute Total Amount of Interest -> Total Amount Paid - Principal
    # Print each of the final amounts 


def interest_over_time ():

 # Initial inputs from the user

    interest = eval(input("What is the percentage of Interest: "))

    principal = eval(input("What is the Initial Loan amount: $"))

    months = eval(input("What is the length of the Loan in Months: "))

 # Math calculations 

    rate = interest / 1200

    monthlyPayment = round((principal * rate * (1 + rate)**months) / ( ( (1 + rate)**months)-1), 2)

    totalAmountPaid = round(monthlyPayment * months, 2)

    totalAmountOfInterest = round(totalAmountPaid - principal, 2)

# Outputs for the user

    print ("Your Monthly Payment will be: $", monthlyPayment, sep='')

    print ("You will pay this amount Overall: $", totalAmountPaid, sep='')

    print ("You will pay this amount of Interest: $", totalAmountOfInterest, sep='')

interest_over_time ()