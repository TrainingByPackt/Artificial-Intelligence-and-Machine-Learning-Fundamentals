# K-Means Clustering with Scikit-Learn

Suppose the following data points are given:

```
import numpy as np 

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
```

The number of clusters is `3`.

Perform K-Means clustering on them using Scikit-Learn. 

Print the cluster centers and labels.

Plot your results on a two dimensional graph, showing the cluster centers of each cluster, and showing each cluster using a different color.

Predict the cluster of the data points `[5,5]` and `[0,10]`.

Perform the above clustering exercises with `2` clusters. Compare your results.