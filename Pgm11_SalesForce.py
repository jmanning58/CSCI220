# Program for user to check on employees sales records and to add new employees
# Jacob Manning
# Paul Rose
 
# Specifications:

    # Class for 'SalesForce':

        # Maintains list of 'SalesPerson' objects
        # Constructor has no parameters and should initialize the list
        # Add data method, (filename) only parameter, input for all the info on the person
            # ID FirstName LastName Sales amounts[a]
        # Quota report method, (quota), prints each person's:
            # ID Name Total sales (regardless if quota has been met)
        # Top Sales method, returns best person in sales
        # Individuals Sales method, (ID) to reference employee:
            # Prints ENTIRE record of sales
            # If ID doesn't matter anyone respond accordingly
 
# Design:

    # __init__ Method(takes only 'self'):

        # Opens to read file, gathers all lines into self._employee, and closes file

    # add_data Method(takes in 'self' and 'filename'):

        # Opens to write to file

        # For loop to gather each line of employee's info:
            # Empty list for storing data
            # For loop to gather sales for each employee
        
        # Print statement to show the user who they're looking at with their info

    # quota_report Method(takes in 'self' and 'quota'):

        # For loop checking to see if each employee has met quota

    # top_sales_person Method(takes only 'self'): - m: not sure yet

    # individual_sale Method(takes in 'self' and 'ID'): - m: not sure yet
 
# Notes:
  
   # Don't forget to import the file 'GradeBook' for reference
   # Consider making a graphics for prgm
   # Make a sorting method

from Pgm11_SalesPerson import *
 
class SalesForce():
 
    def __init__(self):

        self._employees = []
        
    def add_data(self, filename):

        self._employment_info = filename
        with open(filename, 'rt') as openfile:

            for employee in openfile:

                employee_info = employee.split()
                ID = employee_info[0]
                person = ' '.join(employee_info[1:3])
                sales = employee_info[3:]
                sales_rep = SalesPerson(ID, person, sales)
                self._employees.append(sales_rep)

    def quota_report(self, quota):

        for employee in self._employees:
            the_goal = employee.met_quota(quota)
            print(employee, "Quota met? "+str(the_goal))
 
    def top_sales_person(self):

        top_person = SalesPerson(000,'',[])

        for i in range(len(self._employees)-1):
            is_higher = self._employees[i].compare_to(self._employees[i+1])

            if is_higher == True or is_higher == -1:
                if self._employees[i].total_sales() > top_person.total_sales():
                    top_person = self._employees[i]
            
            elif is_higher == False:
                if self._employees[i+1].total_sales() > top_person.total_sales():
                    top_person = self._employees[i+1]

        return top_person
 
    def individual_sale(self, ID):

        for employee in self._employees:
            if int(employee.get_ID()) == ID:
                print(str(employee.get_sales())+' '+str(employee.total_sales()))
                return
            
        print("There is no employee with that ID number.")