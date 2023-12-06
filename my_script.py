import matplotlib.pyplot as plt
import random
import numpy as np



lst = [random.randint(0, 300) for _ in range(20)]

plt.plot(lst, 'r')
plt.show()


point= np.array([[1, 4],
                 [3, -6],
                 [23, 5],
                 [10, 4]])

print(point.shape)