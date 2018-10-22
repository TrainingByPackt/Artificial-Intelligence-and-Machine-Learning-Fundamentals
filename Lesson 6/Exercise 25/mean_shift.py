import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plot

dataPoints = np.array([
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

MeanShiftModel = MeanShift()
MeanShiftModel.fit(dataPoints)

print('Cluster centers: ', MeanShiftModel.cluster_centers_)
print('\n')
print('Labels', MeanShiftModel.labels_)
print('\n\n')

plot.scatter(
    MeanShiftModel.cluster_centers_[:, 0],
    MeanShiftModel.cluster_centers_[:, 1]
)

for i in range(len(dataPoints)):
    plot.plot(
        dataPoints[i][0],
        dataPoints[i][1],
        ['ro', 'go', 'yo', 'ko', 'mo'][MeanShiftModel.labels_[i]]
    )
plot.show()


print('Prediction [(5,5),(0,10)]: ', MeanShiftModel.predict([[5, 5], [0, 10]]))
