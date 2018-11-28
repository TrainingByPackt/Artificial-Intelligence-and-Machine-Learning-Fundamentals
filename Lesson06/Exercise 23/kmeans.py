import numpy as np
from sklearn.cluster import KMeans
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


print('--------------------------')
print('K-Means with 3 clusters: ')
print('\n')

k_means_model = KMeans(n_clusters=3)
k_means_model.fit(data_points)

print('Cluster centers: ', k_means_model.cluster_centers_)
print('\n')
print('Labels', k_means_model.labels_)
print('\n\n\n')

plot.scatter(
    k_means_model.cluster_centers_[:, 0],
    k_means_model.cluster_centers_[:, 1]
)

for i in range(len(data_points)):
    plot.plot(
        data_points[i][0],
        data_points[i][1],
        ['ro', 'go', 'yo'][k_means_model.labels_[i]]
    )
plot.show()

print('Prediction [(5,5),(0,10)]: ', k_means_model.predict([[5, 5], [0, 10]]))
print('\n\n\n')

print('--------------------------')
print('K-Means with 2 clusters: ')
print('\n')

k_means_model = KMeans(n_clusters=2)
k_means_model.fit(data_points)

print('Cluster centers: ', k_means_model.cluster_centers_)
print('\n')
print('Labels', k_means_model.labels_)
print('\n\n\n')

plot.scatter(
    k_means_model.cluster_centers_[:, 0],
    k_means_model.cluster_centers_[:, 1]
)

for i in range(len(data_points)):
    plot.plot(
        data_points[i][0],
        data_points[i][1],
        ['ro', 'go'][k_means_model.labels_[i]]
    )
plot.show()
