import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
	pop_data = pd.read_csv("D:\Py\_PyStatistics\WB_DataSet\_Pop_by_Country.csv")
except Exception as e:
	print(str(e))


gdp_cap = []
life_exp = []
pop = []

# Specify c and alpha inside plt.scatter()
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k','10k','100k'])

# Show the plot
plt.show()
