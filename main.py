# Data Source: https://www.wunderground.com/history/monthly/us/ga/atlanta/KATL/date/2021-12

# Imports Numpy for data arrays
import numpy as np
# Imports Matplotlib to plot and create a graph from the arrays
import matplotlib.pyplot as plt

# An array of the x values
# The x values represent the number of months
a = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    dtype='i'
)

# An array of the y values
# The y values represent the average temperature
b = np.array(
    [49.28, 49.5, 60.82, 61.56, 68.52, 75.73, 81.06, 79.21, 72.83, 66.67, 58.37, 46.06, 46.13, 47.58, 59.07, 62.67, 69.57, 76.49, 78.65, 78.91, 73.49, 66.18, 52.42, 55.5], 
    dtype='f'
)
print(a)
print(b)

plt.plot(a, b, label = "original")
plt.title('Average Temperature Over 2 Years (2020 - 2021)')
plt.xlabel('Months (1 - 24)')
plt.ylabel('Average Temperature')
plt.legend()
plt.show()