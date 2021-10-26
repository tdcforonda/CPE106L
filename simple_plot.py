import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1.5, 10)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.annotate('intersection', (1,1))

plt.xlabel('x value')
plt.ylabel('y value')
plt.title("Simple Plot")
plt.legend()
plt.show()