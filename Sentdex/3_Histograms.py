import matplotlib.pyplot as plt

'''
    Bar charts show the comparison of different variable,
    they are discrete.
    ex: Number of speakers of different languages
    
    While Histograms show the distribution of variables,
    they are continuous.
    ex: GPD of a Country by Year
'''
# Data for Histogram:
pop_ages = [22, 55, 62, 45, 65, 74, 12, 15, 32, 115, 30, 22, 14, 24, 53, 36, 12, 5, 32, 25, 27, 86, 95, 90, 111, 30]
''' To make BarChart for this:
ids = [x for x in range(len(pop_ages))]
plt.bar(ids, pop_ages, label='Ugly Bar Chart!')
'''
# Making AgeGroups for Histograms x axis
# bins is any group/class we assign
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
# Histogram: plt.hist(y axis, bins) other args (label, color, histtype, rwidth)
plt.hist(pop_ages, bins, label='Population distribution', color='b', histtype='bar', rwidth=0.8)

plt.xlabel('Plot Number')                   # Labels x axis
plt.ylabel('Important variable! (Units)')   # Labels y axis
plt.title('Histogram Lesson!')              # Title of the Graph
plt.legend()                                # Showing legend (labels for each line)

plt.show()
