import matplotlib.pyplot as plt

'''
    Bar charts show the comparison of different variable,
    they are discrete.
    ex: Number of speakers of different languages
    
    While Histograms show the distribution of variables,
    they are continuous.
    ex: GPD of a Country by Year
'''
# Data for Bar_1
x = [2, 4, 6, 8, 10]
y = [6, 4, 9, 5, 13]
# Data for Bar_2
x2 = [1, 3, 5, 9, 11]
y2 = [7, 8, 15, 12, 10]

# For BarChart: plt.bar(x, y, label, color)
plt.bar(x, y, label="Bar_1", color='y')
plt.bar(x2, y2, label='Bar_2', color='teal')

plt.xlabel('Plot Number')                   # Labels x axis
plt.ylabel('Important variable! (Units)')   # Labels y axis
plt.title('Bar Graph Lesson!')              # Title of the Graph
plt.legend()                                # Showing legend (labels for each line)

plt.show()
