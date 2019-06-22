import matplotlib.pyplot as plt

pop_ages = [22, 55, 62, 45, 65, 74, 12, 15, 32, 115, 30, 22, 14, 24, 53, 36, 12, 5, 32, 25, 27, 86, 95, 90, 111, 30]
bins = range(0, 120, 15)

x = [2, 4, 6, 8, 10]
y = [6, 4, 9, 5, 13]

companies = ['Apple', 'Microsoft', 'IBM', 'Space X']
comp_color = ['grey', 'blue', 'cyan', 'black']
revenue = [120000, 130000, 110000, 95000]
rev_lab = ['12M', '13M', '11M', '95k']

# Format: plt.bar(x, y, color=color_array[], label='labels for each element'<String>)
plt.bar(companies, revenue, color=comp_color, label='Top Tech Company Revenues')
plt.ylabel('Dollars($)')
plt.title('Top Tech Company Revenue')
plt.show()
