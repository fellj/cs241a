# Title:    Prove Assignment 03
# Filename: assign03.py
# Purpose:  Using python classes to
#           generate a robot program.
#
# Assignment: Prove 03 - https://bit.ly/38VRFbj
#
#
#################################################################################
"""

Write a Python 3 program to model driving a robot around in an environment.
The robot has the following attributes:

    * xcoord

    * y-coordinate

    * fuel amount

It can do the following things:

    1. move left, right, up, and down

    2. display its current status

    3. fire its laser

Initialization:

The robot should begin at location (10, 10),
and should start with a fuel amount of 100.

Member Functions (Methods):

Move:

When told to move, the robot's fuel should decrease by 5,
and it should move one unit in the desired direction
(Left should subtract one from the xcoord and
right should add 1 to the it.
Down should add 1 to the y-coordinate,
and up should subtract one from it).

Status:

Displaying the status should print the location
and fuel to the console in the format:

"(xcoord, y-coordinate) - Fuel: fuel-amount", such as (9, 4) - Fuel: 75.

Fire:

Firing the laser should output "Pew! Pew!"
to the console and reduce the fuel-amount by 15.

Out of fuel:

If the robot does not have enough fuel for
any of the above actions, it should display the text,
"Insufficient fuel to perform action".
In that case it should not move,
fire the laser, or reduce the fuel.

USER INTERFACE

The user is presented with a prompt: "Enter command: "
and can enter any of the following commands:

    * left

    * right

    * up

    * down
    
    * fire

    * status

    * quit

Any other commands should be ignored, and the user re-prompted.
When the user enters the quit command,
the program should display the text, "Goodbye" and then exit.

DESIGN

Your program should demonstrate good object-oriented design principles.
You should use functions for appropriate main interaction,
and a class with appropriate variables and methods (member functions)
to model the robot.

Make sure to use good style including variable names,
function headers, and appropriate comments.
Avoid global variables and other elements of code
that will make your code difficult to read and maintain.


"""

class Robot():
    """
    Robot() - Creates a new robot
              that can perform various
              actions.
    """
    
    def __init__(self):
        
        """ Initializes the new robot with
            location (x:10, y:10) and fuel
            amount (100).
        """
        
        self.xcoord          = 10
        self.ycoord          = 10
        self.fuel            = 100
        self.command         = 0      # represents standby
        self.exit            = False  # exits program when True
        self.insf_msg        = "Insufficient fuel to perform action" 
        
    def left(self):
        """
        left() - the robot instance
                 moves to the left 1
                 unit decreasing fuel
                 by 5.
        """
        fuel_cost = 5
        if not self.fuel - fuel_cost < 0:
            self.xcoord       += 1
            self.fuel         -= fuel_cost

        else:
            print(self.insf_msg)
        
    def right(self):
        """
        right() - the robot instance
                  moves to the right 1
                  unit decreasing the
                  x-coordinate by 1 and
                  fuel by 5.
        """
        fuel_cost = 5
        if not self.fuel - fuel_cost < 0:
            self.xcoord       -= 1
            self.fuel         -= fuel_cost

        else:
            print(self.insf_msg)


    def up(self):
        """
        up() -  the robot instance
                moves up 1
                unit decreasing the
                y-coordinate by 1 and
                fuel by 5.
        """
        fuel_cost = 5
        if not self.fuel - fuel_cost < 0:
            self.ycoord       -= 1
            self.fuel         -= fuel_cost
            
        else:
            print(self.insf_msg)

    def down(self):
        """
        down() - the robot instance
                 moves down 1
                 unit increasing the
                 y-coordinate by 1 and
                 decreasing fuel by 5.
        """
        fuel_cost = 5
        if not self.fuel - fuel_cost < 0:
            self.ycoord     += 1
            self.fuel       -= fuel_cost

        else:
            print(self.insf_msg)            
        
    def fire(self):
        """
        fire() - the robot fires
                 a laser displaying
                 Pew!Pew! and 
                 decreasing fuel by 15.
        """
        fuel_cost = 15
        if not self.fuel - fuel_cost < 0:
            print("Pew! Pew!")
            self.fuel -= fuel_cost
            
        else:
            print(self.insf_msg)           
        
    def status(self):
        """
        status() - displays the robot's
                   coordinates and
                   fuel level.
        """
        open_paren  = "("
        close_paren = ")"
        comma       = ","
        dash        = " - "
        colon       = ":"
        space       = " "
        print(open_paren + str(self.xcoord) + comma + \
              space + str(self.ycoord) + close_paren + \
              dash + "Fuel" + colon + space + \
              str(self.fuel))
        
    # This functions prompts the user to enter a command
    # for the robot
    def get_command(self):
        """
        get_command() - This function prompts the user
                        to enter a command and ignores
                        those not included in the list
                        below:
                       
                        * up
                        * down
                        * right
                        * left
                        * status
                        * fire
                        * quit
        """
        command = {"up":1, "down":2, "right":3, "left":4, "status":5, "fire":6, "quit":7}
        start = 1
        end = len(command) + 1
        while self.command not in range(start, end):
            self.command = command.get(str(input("Enter command: ")))

    # This member function puts the robot
    # in standby mode
    def standby(self):
        """
        standby() - puts the robot in standby
                    mode. Robot is waiting for
                    the next command.
        """
        self.command = 0

    # This member function exits the program
    def quit(self):
        """
        quit() - This function returns a boolean
                 value signaling to end the
                 robot program. It prints "Goodbye".
        """
        print ("Goodbye.")
        self.exit = True
        
# This function executes all of the programs tasks
def main():

    r1 = Robot()
    while r1.exit == False:
        r1.get_command()
        if r1.command == 1:
            r1.up()
            r1.standby()
        elif r1.command == 2:
            r1.down()
            r1.standby()
        elif r1.command == 3:
            r1.left()
            r1.standby()
        elif r1.command == 4:
            r1.right()
            r1.standby()
        elif r1.command == 5:
            r1.status()
            r1.standby()
        elif r1.command == 6:
            r1.fire()
            r1.standby()
        elif r1.command == 7:
            r1.quit()

    

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()