# This program will show a stick figure doing jumping jacks until told to stop
# Jacob Manning

# Specifications:
    # Import time and graphics
    # Create a graphics window
    # Create three interactive buttons
        # First button to start
        # Second button to pause
        # Third button to quit
    # Make a Circle for the head and Lines body
    # Create a function for checking mouse clicks
    # Create a function to visually show movement
    # Only call logic function in main

# Design:
    
    # Import Graphics and Time

    # jumping_jack Function:

        # Call window function
        # Call draw_jack function
        # Call draw_button_bases function
        # Call draw_quit_button function
        # Call draw_start_button function
        # While loop for while window is open:

            # Check if there are any mouse clicks
            # If there is a mouse click, where?
            # If statement to start simulation if there was a click in start_button
            # Elif the quit_button was clicked close(terminate) the program

                # Undraw the start button to make it not visible
                # Call draw_pause_button
                # While loop to run while 'paused' is False:

                    # Move Jack with move_jack function assigned to 'paused'
                    # Check if there is a mouse click
                    # If there is, where?
                    # If in quit_button close(terminate) the simulation
                    # If in pause_button break while loop
                
                # When while loop is broken undraw the pause_button, redraw start_button and jack

    # window Function:

        # Size and Title of window
        # Return window

    # draw_button_bases(takes in 'window'):

        # Creates three rectangles acting as bases for buttons
        # Pause is drawn here because initally button is inactive

    # draw_start_button Function(takes in 'window'):

        # Create a rectangle for button
        # Put 'Start' text within rectangle
        # Return only the button

    # draw_pause_button Function(takes in 'window'):

        # Create a rectangle for button
        # Put 'Pause' text within rectangle
        # Return only the button

    # draw_quit_button Function(takes in 'window'):

        # Create a rectangle for button
        # Put 'Quit' within rectangle
        # return only the button

    # was_clicked Function(takes pt, rect):

        # If loop:
            # if pt == None return False
            # Otherwise run the rest of function
        
        # Get X and Y values of rect
        # Get X and Y values of pt
        # return if pt's X and Y are within rect's X and Y

    # draw_jack Function(takes in 'window'):

        # Create a Circle for the head
        # Create a Line for:
            # Both legs, arms, and body
        # Return:
            # head, right_leg, left_leg, right_arm, left_arm, body

    # move_jack Function(takes in 'jack', 'window', 'pause_button', 'quit_button'):

        # Pull each part of 'jack' as list elements
        # Create a variable for sleep time
        # For loop for moving 'jack' up:
            # Undraw original
            # Redraw new
            # Give ways out of the loop

        # For loop for moving 'jack' down:
            # Undraw the 'jack' going up
            # Redraw as he goes down
            # Give ways out of the loop

        # return False to keep the loop running

    # main Function:
        # Call only jumping_jack

from graphics import *
import time

# Running all of programs logic
def jumping_jack():
    
    # Calling base objects 
    win = window()
    jack = draw_jack(win)
    draw_button_bases(win)
    quit_button = draw_quit_button(win)
    start_button = draw_start_button(win)

    # Keeping program running for as long as window is open
    while win.isOpen():
        clicked = win.checkMouse()

        # If start button was clicked run simulation
        if was_clicked(clicked, start_button):
            start_button.undraw()
            pause_button = draw_pause_button(win)

            paused = False
            # Run simulation as long as no buttons are clicked
            while not paused:
                paused = move_jack(jack, win, pause_button, quit_button) 
                clicked = win.checkMouse()

                # To break out of loop and restart or quit
                if was_clicked(clicked, pause_button):
                    paused = True
                    
                elif was_clicked(clicked, quit_button):
                    win.close()

            # Reassigning objects
            pause_button.undraw()
            start_button = draw_start_button(win)
            jack = draw_jack(win)

        elif was_clicked(clicked, quit_button):
            win.close()

# Graphics window for user to interact with
def window():

    width = 800
    height = 800
    fitness = GraphWin("Jumping Jack", width, height)

    return fitness

# Bases of all buttons
def draw_button_bases(window):

    # Shape and color of the base of the button with text
    button_base1 = Rectangle(Point(50, 660), Point(250, 760))
    button_base1.setOutline('black')
    button_base1.setFill('dark gray')
    button_base1.draw(window)

    # Shape and color of the base of the button with text
    button_base2 = Rectangle(Point(300, 660), Point(500, 760))
    button_base2.setOutline('black')
    button_base2.setFill('dark gray')
    button_base2.draw(window)

    # Text that is displayed
    request = Text(Point(400, 710), "Pause")
    request.setSize(20)
    request.draw(window)

    # Shape and color of the base of the button with text
    button_base = Rectangle(Point(550, 660), Point(750, 760))
    button_base.setOutline('black')
    button_base.setFill('dark gray')
    button_base.draw(window)

    # Instructions for user
    start_instructions = Text(Point(150, 620), 'Click Start to Begin')
    start_instructions.setSize(12)
    start_instructions.draw(window)

    quit_instructions = Text(Point(648, 620), 'Click Quit to Close')
    quit_instructions.setSize(12)
    quit_instructions.draw(window)

# To start the simulation
def draw_start_button(instructions):

    # Shape of the top of the button
    button = Rectangle(Point(60, 670), Point(240, 750))
    button.setOutline('dim gray')
    button.setWidth(4)
    button.setFill('snow')
    button.draw(instructions)

    # Text that is displayed
    request = Text(Point(150, 710), "Start")
    request.setSize(20)
    request.draw(instructions)

    return button

# Only to pause the simulation
def draw_pause_button(instructions):

    # Shape of the top of the button
    button = Rectangle(Point(310, 670), Point(490, 750))
    button.setOutline('dim grey')
    button.setWidth(4)
    button.setFill('snow')
    button.draw(instructions)

    # So we can see "Pause" text on top
    request = Text(Point(400, 710), "Pause")
    request.setSize(20)
    request.draw(instructions)

    return button

# To stop and close the simulation window
def draw_quit_button(instructions):

    # Shape of the top of the button
    button = Rectangle(Point(560, 670), Point(740, 750))
    button.setOutline('dim grey')
    button.setWidth(4)
    button.setFill('snow')
    button.draw(instructions)

    # Text that is displayed
    request = Text(Point(650, 710), "Quit")
    request.setSize(20)
    request.draw(instructions)

    return button

# To restrict the user to only press within an area
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

# What Jack actually looks like
def draw_jack(window):

    # Can't imagine someone without a head
    head = Circle(Point(400, 140), 30)
    head.setFill('black')
    head.draw(window)

    # Sarah Jessica Parker thin
    body = Line(Point(400, 170), Point(400, 300))
    body.setWidth(6)
    body.draw(window)

    # Jack's pea shooters
    shoulders = Point(400, 200)
    right_hand = Point(420, 290)
    right_arm = Line(shoulders, right_hand)
    right_arm.setWidth(4)
    right_arm.draw(window)
    left_hand = Point(380, 290)
    left_arm = Line(shoulders, left_hand)
    left_arm.setWidth(4)
    left_arm.draw(window)

    # Skipped leg day one too many times
    hips = Point(400, 300)
    right_foot = Point(430, 430)
    right_leg = Line(hips, right_foot)
    right_leg.setWidth(4)
    right_leg.draw(window)
    left_foot = Point(370, 430)
    left_leg = Line(hips, left_foot)
    left_leg.setWidth(4)
    left_leg.draw(window)

    # Return body parts of Jack
    return [head, body, right_arm, left_arm, right_leg, left_leg]

# Representing the moving of Jack and checking for button presses
def move_jack(jack, window, pause_button, quit_button):

    # Body parts for reference
    head = jack[0]
    body = jack[1]
    right_arm = jack[2]
    left_arm = jack[3]
    right_leg = jack[4]
    left_leg = jack[5]

    # Speed of jumping jacks
    jump_time = .05

    # Draw and undraw by frame going up
    for i in range(20):
        
        # Undraw Jack as jumping jacks start and for each frame
        head.undraw()
        body.undraw()
        right_arm.undraw()
        left_arm.undraw()
        right_leg.undraw()
        left_leg.undraw()

        # Redrawing each part of Jack but moved
        head_center_X = head.getCenter().getX()
        head_center_Y = head.getCenter().getY()
        head_rad = head.getRadius()
        head = Circle(Point(head_center_X, head_center_Y -1), head_rad)
        head.setFill('black')
        head.draw(window)

        neck_X = body.getP1().getX()
        neck_Y = body.getP1().getY()
        waist_X = body.getP2().getX()
        waist_Y = body.getP2().getY()
        body = Line(Point(neck_X, neck_Y -1), Point(waist_X, waist_Y -1))
        body.setWidth(6)
        body.draw(window)

        shoulder_Y = right_arm.getP1().getY()
        shoulders = Point(400, shoulder_Y -1)

        right_hand_X = right_arm.getP2().getX()
        right_hand_Y = right_arm.getP2().getY()
        right_hand = Point(right_hand_X +5, right_hand_Y -10)
        right_arm = Line(shoulders, right_hand)
        right_arm.setWidth(4)
        right_arm.draw(window)

        left_hand_X = left_arm.getP2().getX()
        left_hand_Y = left_arm.getP2().getY()
        left_hand = Point(left_hand_X -5,left_hand_Y -10)
        left_arm = Line(shoulders, left_hand)
        left_arm.setWidth(4)
        left_arm.draw(window)

        hips_Y = right_leg.getP1().getY()
        hips = Point(400, hips_Y -1)

        right_foot_X = right_leg.getP2().getX()
        right_foot_Y = right_leg.getP2().getY()
        right_foot = Point(right_foot_X +4, right_foot_Y -2)
        right_leg = Line(hips, right_foot)
        right_leg.setWidth(4)
        right_leg.draw(window)

        left_foot_X = left_leg.getP2().getX()
        left_foot_Y = left_leg.getP2().getY()
        left_foot = Point(left_foot_X -4, left_foot_Y -2)
        left_leg = Line(hips, left_foot)
        left_leg.setWidth(4)
        left_leg.draw(window)

        # Checking for mouse clicks to close
        clicked = window.checkMouse()
        if was_clicked(clicked, quit_button):
            window.close()

        # Checking for mouse clicks to exit loop
        if was_clicked(clicked, pause_button):
            head.undraw()
            body.undraw()
            right_arm.undraw()
            left_arm.undraw()
            right_leg.undraw()
            left_leg.undraw()
            return True

        time.sleep(jump_time)

    # Draw and undraw by frame going down
    for i in range(20):

        # Undraw Jack as jumping jacks start and for each frame
        head.undraw()
        body.undraw()
        right_arm.undraw()
        left_arm.undraw()
        right_leg.undraw()
        left_leg.undraw()

        # Redrawing each part of Jack but moved
        head_center_X = head.getCenter().getX()
        head_center_Y = head.getCenter().getY()
        head_rad = head.getRadius()
        head = Circle(Point(head_center_X, head_center_Y +1), head_rad)
        head.setFill('black')
        head.draw(window)

        neck_X = body.getP1().getX()
        neck_Y = body.getP1().getY()
        waist_X = body.getP2().getX()
        waist_Y = body.getP2().getY()
        body = Line(Point(neck_X, neck_Y +1), Point(waist_X, waist_Y +1))
        body.setWidth(6)
        body.draw(window)

        shoulder_Y = right_arm.getP1().getY()
        shoulders = Point(400, shoulder_Y +1)

        right_hand_X = right_arm.getP2().getX()
        right_hand_Y = right_arm.getP2().getY()
        right_hand = Point(right_hand_X -5, right_hand_Y +10)
        right_arm = Line(shoulders, right_hand)
        right_arm.setWidth(4)
        right_arm.draw(window)

        left_hand_X = left_arm.getP2().getX()
        left_hand_Y = left_arm.getP2().getY()
        left_hand = Point(left_hand_X +5,left_hand_Y +10)
        left_arm = Line(shoulders, left_hand)
        left_arm.setWidth(4)
        left_arm.draw(window)

        hips_Y = right_leg.getP1().getY()
        hips = Point(400, hips_Y +1)

        right_foot_X = right_leg.getP2().getX()
        right_foot_Y = right_leg.getP2().getY()
        right_foot = Point(right_foot_X -4, right_foot_Y +2)
        right_leg = Line(hips, right_foot)
        right_leg.setWidth(4)
        right_leg.draw(window)

        left_foot_X = left_leg.getP2().getX()
        left_foot_Y = left_leg.getP2().getY()
        left_foot = Point(left_foot_X +4, left_foot_Y +2)
        left_leg = Line(hips, left_foot)
        left_leg.setWidth(4)
        left_leg.draw(window)

        # Checking for mouse clicks to close
        clicked = window.checkMouse()
        if was_clicked(clicked, quit_button):
            window.close()

        # Checking for mouse clicks to exit loop
        if was_clicked(clicked, pause_button):
            head.undraw()
            body.undraw()
            right_arm.undraw()
            left_arm.undraw()
            right_leg.undraw()
            left_leg.undraw()
            return True

        time.sleep(jump_time)
   
   # Undraw new Jack so we can start over
    head.undraw()
    body.undraw()
    right_arm.undraw()
    left_arm.undraw()
    right_leg.undraw()
    left_leg.undraw()
    
    return False

# Main function calling the logic function
def main():
    jumping_jack()

main()