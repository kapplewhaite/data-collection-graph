# Imports Numpy for data arrays
import numpy as np
# Imports Matplotlib to plot and create a graph from the arrays
import matplotlib.pyplot as plt

# Sets evenly spaced points from 1 to 24 to represent months
c = np.linspace(1, 24, 100)

# A sine equation that predicts the average temperature over 2 years
d = 18.9 * np.sin((np.pi / 12) * c - (np.pi / 12)) + 61.7

# Plots the data points
plt.plot(c, d, label = "Prediction")
plt.show()