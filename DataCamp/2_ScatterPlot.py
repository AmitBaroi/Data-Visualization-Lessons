import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

plt.scatter(year, pop)

# Customization:
plt.title("Global Population growth (1940-2100)")
plt.xlabel("Year")
plt.ylabel("Population")

# Display the plot:
plt.show()
