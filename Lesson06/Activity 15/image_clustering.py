from PIL import Image
import pandas
from sklearn.cluster import KMeans, MeanShift

INPUT_FILE = 'destructuring.jpg'

# 1. Reading the image
image = Image.open(INPUT_FILE)
pixels = image.load()

# 2. Building a data frame from the image
data_frame = pandas.DataFrame(
    [[x, y, pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]]
        for x in range(image.size[0])
        for y in range(image.size[1])
     ],
    columns=['x', 'y', 'r', 'g', 'b']
)

# 3. Mean Shift model fitting
mean_shift_model = MeanShift()
mean_shift_model.fit(data_frame)


# 4. Mean Shift: creating image clusters
def create_image_clusters(model, output_file_name):
    for i in range(len(model.cluster_centers_)):
        image = Image.open(INPUT_FILE)
        pixels = image.load()
        for j in range(len(data_frame)):
            if (model.labels_[j] != i):
                pixels[int(data_frame['x'][j]), int(
                    data_frame['y'][j])] = (255, 255, 255)
        image.save(output_file_name + str(i) + '.jpg')


create_image_clusters(mean_shift_model, 'meanshift_cluster')

# 5. K-means model fitting with specified number of clusters
k_means_model = KMeans(n_clusters=8)
k_means_model.fit(data_frame)

# 6. K-means: creating image clusters
create_image_clusters(k_means_model, 'kmeans_cluster')
