import numpy as np
from numpy import mean
import matplotlib.pyplot as plot

x = np.array(range(1, 14))
y = np.array([2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62])

a = (mean(x)*mean(y) - mean(x*y)) / (mean(x) ** 2 - mean( x ** 2 ))
b = mean(y) - a*mean(x)

plot.scatter( x, y )
plot.plot( [0, 15], [b, 15*a+b] )
plot.show()