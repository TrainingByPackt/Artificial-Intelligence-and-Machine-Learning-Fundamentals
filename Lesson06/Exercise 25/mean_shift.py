import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plot

data_points = np.array([
    [1, 1],
    [1, 1.5],
    [2, 2],
    [8, 1],
    [8, 0],
    [8.5, 1],
    [6, 1],
    [1, 10],
    [1.5, 10],
    [1.5, 9.5],
    [10, 10],
    [1.5, 8.5],
])


print('Mean Shift clustering: ')

mean_shift_model = MeanShift()
mean_shift_model.fit(data_points)

print('Cluster centers: ', mean_shift_model.cluster_centers_)
print('\n')
print('Labels', mean_shift_model.labels_)
print('\n\n')

plot.scatter(
    mean_shift_model.cluster_centers_[:, 0],
    mean_shift_model.cluster_centers_[:, 1]
)

for i in range(len(data_points)):
    plot.plot(
        data_points[i][0],
        data_points[i][1],
        ['ro', 'go', 'yo', 'ko', 'mo'][mean_shift_model.labels_[i]]
    )
plot.show()


print('Prediction [(5,5),(0,10)]: ', mean_shift_model.predict([[5, 5], [0, 10]]))
