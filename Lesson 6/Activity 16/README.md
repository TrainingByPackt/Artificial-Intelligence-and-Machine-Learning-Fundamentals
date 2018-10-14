# Shape recognition with the Mean Shift and K-Means algorithms

We will be assuming that you are working for a company detecting human emotions from photos. Your task is to extract pixels making up a face in an avatar photo. 

Create a clustering algorithm with Mean Shift to cluster pixels of images. Examine the results of the Mean Shift algorithm and check if any of the clusters contains a face when used on avatar images. 

​Then apply the K-Means algorithm with a fixed default number of clusters: 8. Compare your results with the Mean Shift clustering algorithm. 

Use the image `Destructuring.jpg` provided in this folder.

Save the images to the disk.

## Remark on the execution

Allow a few minutes for the algorithm to complete. Even though I shrinked the image as much as possible, real world examples require more computing power than classroom examples.

Solution: `image_clustering.py`.