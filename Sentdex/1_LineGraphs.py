import matplotlib.pyplot as plt

# Example data-sets:
x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

# For line plot: plt.plot(x, y, label)
# Since we have 2 line plots we give them each a name (label) to identify them:
plt.plot(x, y, label='First Graph!')
plt.plot(x2, y2, label='Second Graph!')
plt.xlabel('Plot Number')                   # Labels x axis
plt.ylabel('Important variable! (Units)')   # Labels y axis
plt.title('First Python Graph!')            # Title of the Graph
plt.legend()                                # Showing legend (labels for each line)

plt.show()                                  # Renders the plot visible
