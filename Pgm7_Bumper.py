# This program shows two cars, represented by circles, avoiding each other, and the walls
# Jacob Manning

# Specification:

    # Import Graphics
    # Import Time
    # Import Random
    # Create a graphics window
    # Give instructions for user
    # Create button to initiate simulation
    # Create circles that:
        # move randomly
        # operate off of boolean 
        # bounce off of each other and edges of window

# Design:
    # Import graphics, random, time, and math

    # bumper_car Function:
        # Call window function
        # Call button function for interactive button
        # Call moving_circles to generate circles

    # window Function:
        # Size of window
        # Title of window
        # Return the window as 'driving_course'

    # button Function(takes in 'driving_course'):
        # Creates a button (that is almost interactive)
        # While loop to make the program wait for user to click the button
        # Undraw the button so it doesn't remain while simulation is active

# Notes:
    # Import Graphics
    # Create window
    # Create two Circles
    # If statments for walls
    # If statments for each other
    # Think about a button to start

from graphics import *
from random import *
import time
import math

def bumper_car():

    driving_course = window()
    make_button = button(driving_course)
    make_circles = moving_circles(driving_course)
    driving_course.getMouse()
    driving_course.close()

def window():

    width = 500
    height = 500
    driving_course = GraphWin("Bumper Cars", width, height)

    return driving_course

# Button to start the simulation
def button(instructions):

    # Shape and color of the base of the button with text
    button_base = Rectangle(Point(180, 210), Point(320, 290))
    button_base.setOutline('black')
    button_base.setFill('gray')
    button_base.draw(instructions)

    # Shape of the top of the button
    button = Rectangle(Point(190, 220), Point(310, 280))
    button.setOutline('grey')
    button.setFill('snow')
    button.draw(instructions)

    # Text that is displayed
    request = Text(Point(250, 250), "Click to Run")
    request.draw(instructions)
    
    # For loop run indefinitly
    x = False

    # To show clicking in button
    while x == False:
        pt = instructions.getMouse()

        # To break out of the loop
        if in_button(pt, button):
            x = True

    # Gets rid of the buttons to start the simulation
    if x == True:
        request.undraw()
        button.undraw()
        button_base.undraw()

# Made to check if in button
def in_button(the_pt, top_button):

    x1 = top_button.getP1().getX()
    x2 = top_button.getP2().getX()

    y1 = top_button.getP1().getY()
    y2 = top_button.getP2().getY()

    px = the_pt.getX()
    py = the_pt.getY()

    return x1 < px < x2 and y1 < py < y2

def moving_circles(driving_course):

    # The "cars" that we'll be demonstrating
    car1 = Circle(Point(randint(20, 480), randint(20, 480)), 20)
    car1.setFill('blue')
    car1.draw(driving_course)
    car2 = Circle(Point(randint(20, 480), randint(20, 480)), 20)
    car2.setFill('black')
    car2.draw(driving_course)

    # The speed in which the circles move
    car1_movement = choice([-5,5])
    car2_movement = choice([-5,5])
    wait_time = .05

    # Run driving simulation til told to quit
    while driving_course.isOpen():
        
        # Cool, you're still on the road
        car1.move(car1_movement, car1_movement)
        car2.move(car2_movement, car2_movement)

        # How's driver one doing?
        if at_edge(car1, driving_course):
            car1_movement *= -1
        
        # How's driver two doing?
        if at_edge(car2, driving_course):
            car2_movement *= -1
        
        # Exchange insurance?
        if collision(car1, car2):
            car1_movement *= -1
            car2_movement *= -1
        
        time.sleep(wait_time)

    # You want off this ride
    
# Calculates where the circle is within the window
def at_edge(car, window):

    # The max values of the window
    right_max = window.getWidth()
    bottom_max = window.getHeight()

    # Coorodinates of circles center and size
    center_x = car.getCenter().getX()
    center_y = car.getCenter().getY()
    car_size = car.getRadius()
    
    # Full radius of circle
    passenger_side = car_size + center_x
    drivers_side = center_x - car_size
    front_bumper = center_y - car_size
    trunk = car_size + center_y

    # Are you about to go off the road?
    in_grass = passenger_side >= right_max
    oncoming_traffic = drivers_side <= 0
    construction = front_bumper <= 0
    ditch = trunk >= bottom_max

    return in_grass or oncoming_traffic or construction or ditch


# Check if the circles hit
def collision(first_car, second_car):

    # Where was your car and what was your model?
    car1_x = first_car.getCenter().getX()
    car1_y = first_car.getCenter().getY()
    car1_size = first_car.getRadius()

    # Where was your car and what was your model?
    car2_x = second_car.getCenter().getX()
    car2_y = second_car.getCenter().getY()
    car2_size = second_car.getRadius()

    # How far about are the cars?
    distance = math.sqrt(((car1_x - car2_x)**2)+((car1_y - car2_y)**2))
    total_size_of_cars = car1_size + car2_size
    impact = distance <= total_size_of_cars

    return impact
    
def main():
    bumper_car()

main()