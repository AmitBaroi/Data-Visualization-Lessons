import matplotlib.pyplot as plt
import csv

"""
Reading data from files using the csv module!
"""

x = []
y = []

# Reading the csv text file
with open('data\example.txt', mode='r') as file:
    plots = csv.reader(file, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Reading data using CSV module!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph!\nCheck it out!')
plt.legend()
plt.show()
