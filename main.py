import numpy as np
import matplotlib.pyplot as plt

a = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    dtype='i'
)

b = np.array(
    [63.4, 58.4, 45.1, 45.7, 48.8, 43.5, 41.7, 39.7, 35.6, 38.5, 42.0, 41.0, 38.8, 44.0, 47.5, 37.5, 41.4, 43.5, 48.3, 49.6, 48.9, 47.9, 48.1, 51.7, 56.4, 64.2, 53.7, 39.7, 39.4, 41.8, 44.2], 
    dtype='f'
)
print(a)
print(b)

plt.plot(a, b, label = "original")
plt.title('Average Temperature in January (2021)')
plt.xlabel('Days')
plt.ylabel('Average Temperature')
plt.legend()
plt.show()