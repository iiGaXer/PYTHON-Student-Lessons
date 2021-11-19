import matplotlib.pyplot as plt #! Importing a special function, especially for ploting and math.

input_values = [1, 2, 3, 4, 5] #* A list
sqaures = [1, 4, 9, 16, 25] #* A list
plt.plot(input_values, sqaures, linewidth=5) #! It's used to make a 2D hexagonal binning plot of points x, y.

#! Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#! Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show() #? Shows the plot.
