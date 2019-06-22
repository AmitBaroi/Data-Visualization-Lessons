import matplotlib.pyplot as plt

"""
StackPlots kind of like LinePlots but with polygons.
They are use to show the relative percentage of some categories or classes.
"""
# X axis
days = [1, 2, 3, 4, 5]
# Y axis classes / categories
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [2, 4, 5, 6, 4]

# Format: stackplot(x, args..., kwargs)  !!StackPlots dont have label kwargs!!
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'b'])

# Giving labels (Since stackplot doesnt have label kwarg we fake it with empty lineplots)
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='b', label='Playing', linewidth=5)

plt.xlabel('Day Number')                  # Labels x axis
plt.ylabel('Hours Spent on Activities')   # Labels y axis
plt.title('Stack Plot Lesson!')           # Title of the Graph
plt.legend()
plt.show()
