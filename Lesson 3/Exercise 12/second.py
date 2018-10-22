import matplotlib.pyplot as plot
import numpy as np

# Second dataset:
x2 = np.array(range(1, 14))
y2 = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

deg1 = np.polyfit(x2, y2, 1)
# array([  9.12087912, -34.92307692])
f1 = np.poly1d(deg1)

deg2 = np.polyfit(x2, y2, 2)
# array([  1.75024975, -15.38261738,  26.33566434])
f2 = np.poly1d(deg2)

deg3 = np.polyfit(x2, y2, 3)
# array([  0.2465035 ,  -3.42632368,  14.69080919, -15.07692308])
f3 = np.poly1d(deg3)

plot.plot(
    x2, y2, 'o',  # blue dots
    x2, f1(x2),  # orange
    x2, f2(x2),  # green
    x2, f3(x2)  # red
)
plot.show()
