import matplotlib.pyplot as plt

# Attributes for pie chart
slices = [7, 2, 2, 13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
colors = ['c', 'm', 'g', 'orange']
explode = [0.05, 0.1, 0.08, 0]

# Making Pie Chart
plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,                # Adds a shadow under the pie
        explode=explode,            # Takes a piece of the pie out
        autopct="%1.1f")            # Displays percentages
plt.title('Pie Chart Lesson!')
plt.show()
