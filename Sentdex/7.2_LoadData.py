import matplotlib.pyplot as plt
import numpy as np

"""
Reading data from files using the numpy module!
"""

x, y = np.loadtxt('data\example.txt', delimiter=',', unpack=True)

plt.plot(x, y, label="Reading data using Numpy module!")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph!\nCheck it out!')
plt.legend()
plt.show()
