#!/usr/bin/python3

class Robot:
    """Represents a robot, with a name"""

    # A class variable, counting number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))


        # When this person is created, the robot
        # adds to the population
        Robot.population += 1


    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} of Robots working.".format(Robot.population))


    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

driod1 = Robot("R2-D2")
driod1.say_hi()
Robot.how_many()

driod2 = Robot("C-3PO")
driod2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finised their work. So let's destroy them.")

driod1.die()
driod2.die()

Robot.how_many()
