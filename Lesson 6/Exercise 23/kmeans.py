import numpy as np 
from sklearn.cluster import KMeans
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


print( 'K-Means with 3 clusters: ' )

kMeansModel = KMeans(n_clusters=3) 
kMeansModel.fit( dataPoints )

print( 'Cluster centers: ', kMeansModel.cluster_centers_ )
print( 'Labels', kMeansModel.labels_ )

plot.scatter( 
    kMeansModel.cluster_centers_[:,0],  
    kMeansModel.cluster_centers_[:,1] 
) 

for i in range( len( dataPoints ) ):  
    plot.plot(  
        dataPoints[i][0],  
        dataPoints[i][1],  
        ['ro','go','yo'][kMeansModel.labels_[i]]   
    ) 
plot.show()

print( 'Prediction [(5,5),(0,10)]: ', kMeansModel.predict( [[5,5],[0,10]] ) )

print( '\n\n\nK-Means with 2 clusters: ' )

kMeansModel = KMeans(n_clusters=2) 
kMeansModel.fit( dataPoints )

print( 'Cluster centers: ', kMeansModel.cluster_centers_ )
print( 'Labels', kMeansModel.labels_ )

plot.scatter( 
    kMeansModel.cluster_centers_[:,0],  
    kMeansModel.cluster_centers_[:,1] 
) 

for i in range( len( dataPoints ) ):  
    plot.plot(  
        dataPoints[i][0],  
        dataPoints[i][1],  
        ['ro','go'][kMeansModel.labels_[i]]   
    ) 
plot.show()