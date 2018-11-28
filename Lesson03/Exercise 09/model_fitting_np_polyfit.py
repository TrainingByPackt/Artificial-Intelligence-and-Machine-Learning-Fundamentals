import numpy as np
import matplotlib.pyplot as plot

x = np.array(range(1, 14))
y = np.array([2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62])

[a, b] = np.polyfit(x, y, 1)

plot.scatter(x, y)
plot.plot([0, 15], [b, 15*a+b])
plot.show()
