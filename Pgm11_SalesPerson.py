# This program runs a variety of data calculations for Sales representatives
# Jacob Manning
# Paul Rose
 
# Specifications:
 
    # Class for 'SalesPerson':

        # Name(str), ID attached(int), and sales list(flt) methods
        # Creation of sales method
        # Getting the sales method(list), copy not alias
        # Getter methods for ID, name, and sales
        # Method to sum up total sales
        # Quota method(bool), to check if they've met sales goal
        # Comparison method, check against another person
 
# Design:
 
    # SalesPerson class:

        # __init__ Method(takes in 'self', 'ID', 'name', and 'sales'):

            # Empty list for employees
            # Assign each parameter to a self._(variable)
            # Append all to empty list

        # __str__ Method(takes only 'self'):

            # Formats the employee - ID, Name, and Total sales into a string

        # get_ID Method(takes only 'self'):

            # Returns the employee's ID number

        # get_name Method(takes only 'self'):

            # Returns Name

        # get_sales Method(takes only 'self'):

            # If statementfor in case employee has no sales

                # Return '0'

            # Returns a copy of employee's list of sales

        # set_name Method(takes 'self' and 'new_name'):

            # Alters the orginal name to the 'new_name'

        # enter_sale Method(takes in 'self' and 'a_sale'):

            # Appends a new sale to 'self._sales'

        # total_sales Method(takes in 'self' and 'all_sales'):

            # Assigns all of employee's sales to a variable
            # For loop to add up all sales
            # Returns total

        # met_quota Method(takes in 'self' and 'quota'):

            # If statement checking employee's total sales against input number:
                # returns True if so

            # Else statement returning False if they haven't

        # compare_to Method(takes in 'self' and 'other_person'):

            # Returns the higher sales of either original person or other person
 
class SalesPerson:
 
    # Method that initiates upon use
    def __init__(self, ID, name, sales):
 
        # Assigning instances for other methods to use
        self._ID = ID
        self._name = name
        self._sales = sales

    # Making all the information viewable in a nice line
    def __str__(self):
 
        employee_ID = "{:3s}".format(self.get_ID())
        employee = "{:4.20s}".format(self.get_name())
        employee_sales = "{:.2f}".format(self.total_sales())
        
        # Returning line for format
        return 'ID - '+employee_ID+'   Employee - '+employee+'   Total Sales - $'+employee_sales
 
    # Method for getting employee's ID
    def get_ID(self):

        return self._ID
 
    # Method for getting employee's name
    def get_name(self):
        
        return self._name
 
    # Obtaining a list of all the employee's sales
    def get_sales(self):
 
        # If they have yet to make a sell return '0'
        if self._sales == None:
            return 0

        return self._sales
 
    # Altering employee's name
    def set_name(self, new_name):

        self._name = new_name

    # Adding a new sale to employee's record
    def enter_sale(self, a_sale):
 
        self._sales.append(a_sale)
    
    # Suming up all of employee's sales
    def total_sales(self):
 
        sales = self.get_sales()
        total = 0

        for i in range(len(sales)):
            total += float(sales[i])

        return total

    # Checking if employee has met quota
    def met_quota(self, quota):

        if self.total_sales() >= quota:
            return True

        else:
            return False

    # Checking employee's against each other 
    def compare_to(self, other_person):
        
        employee_one = self.total_sales()
        employee_two = other_person.total_sales()

        if employee_one > employee_two:
            return True

        if employee_one < employee_two:
            return False

        # If both have the same sales
        return -1

# # Testing
# def main():

    #     bunch_of_sales = [32.58, 44.09, 345.87]
    #     ton_of_sales = [32.58, 44.09, 345.87]
    #     employee = SalesPerson(123, 'Bob Ross', bunch_of_sales)
    #     employee.enter_sale(50.00)
    #     print(employee)
    #     print(employee.get_sales())
    #     print(employee.met_quota(300.00))
    #     print(employee.met_quota(500.00))
    #     new_employee = SalesPerson(465, 'Scott Sterling', ton_of_sales)
    #     new_employee.enter_sale(51.00)
    #     print(new_employee)
    #     print(new_employee.get_sales())
    #     print(employee.met_quota(300.00))
    #     print(employee.met_quota(500.00))
    #     print(employee.compare_to(new_employee))
    #     employee.set_name('American Man')
    #     print(employee)

# main()