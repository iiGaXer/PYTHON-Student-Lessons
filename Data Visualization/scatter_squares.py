import matplotlib.pyplot as plt #! Importing a special function, especially for plotting data.

x_values = list((range(1, 1001))) #* A list: the x values
y_values = [x**2 for x in x_values] #* A list: the y values

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40) #! It plots the points

#! Sets chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#! Sets size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

#! Sets the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show() #* Shows the point

plt.savefig('squares_plot.png', bbox_inches='tight')