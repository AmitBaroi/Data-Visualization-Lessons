import matplotlib.pyplot as plt

x = [1, 5, 9, 7, 3, 4, 3, 8, 1, 3, 8, 4, 2, 5]
y = [1, 6, 8, 6, 4, 2, 5, 5, 3, 3, 5, 4, 3, 9]

# ScatterPlots: plt.scatter(x, y) keyArgs(label, color, marker=['o', 'x', '*'], s(MarkerSize))
# Google for more Marker and Size options

plt.scatter(x, y, label='DataPoints!', color='k', marker='x', s=50)

plt.xlabel('X')                             # Labels x axis
plt.ylabel('Y')                             # Labels y axis
plt.title('Scatter Plot Lesson!')           # Title of the Graph
plt.legend()                                # Showing legend (labels for each line)

plt.show()
