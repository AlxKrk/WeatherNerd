import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.1)
y = x

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='time', ylabel='temperature',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()