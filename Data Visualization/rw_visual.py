import matplotlib.pyplot as plt #! Importing a special function, especially for ploting and math.

from random_walk import RandomWalk #* Imports the necessary functions needed.

while True:
    #! Makes a random walk, and plots the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    #* Set the size of the plotting window.
    plt.figure(figsize=(10, 6))


    point_numbers = list(range(rw.num_points)) #* Generates a list of random numbers that of the number of points
    #? -in the walk

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15) #! Scatters
    #? -those values or color, anything in the "()"

    #! Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  


    plt.show()

    continuation = input("Make another walk? (y/n): ") #* A input variable
    #! They'll ask (y/n) if they want to make another random walk, if so..:
    if continuation == 'n' or 'N':
        break

