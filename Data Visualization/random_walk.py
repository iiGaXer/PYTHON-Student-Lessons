from random import choice #! Creates the necessary functions and enent handlers to make a random walk

#! A "random walk" is a path that has no clear direction but is determined by a series of random decisions-
#? -each of which is left entirely to chance.

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points 

        #! All walks start at (0, 0)
        self.x_values = [0] #? The x-coordinate value 
        self.y_values = [0] #? The y-coordinate value

    def fill_walk(self):
        """Calculate all the points in the walk"""

        #! Keep waking steps until the walk reaches.
        while len(self.x_values) < self.num_points:
            #* For lines 20-23: Decides which direction to go and how far to go in that direction.
            #* This chooses a value for x for x_direction: returning 1 for right movement and -1 for left.
            x_direction = choice([1, -1]) 
            #* How far to move IN that direction (x_distance) by randomly selecting an integer between 0 and 4
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            #? Read lines 19, 22 and 20 for more info.
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #! Rejects moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #! Calculates the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

            

