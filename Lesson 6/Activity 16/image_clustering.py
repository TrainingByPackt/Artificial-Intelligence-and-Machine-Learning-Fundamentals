from PIL import Image
import pandas 
from sklearn.cluster import MeanShift 

image = Image.open('destructuring.jpg') 
pixels = image.load()

dataFrame = pandas.DataFrame(  
    [[x,y,pixels[x,y][0], pixels[x,y][1], pixels[x,y][2]]  
        for x in range(image.size[0])  
        for y in range(image.size[1])  
    ],  
    columns=['x', 'y', 'r', 'g', 'b' ]
)

MeanShiftModel = MeanShift() 
MeanShiftModel.fit( dataFrame )

for i in range( len( MeanShiftModel.cluster_centers_ ) ): 
    image = Image.open('destructuring.jpg') 
    pixels = image.load() 
    for j in range( len( dataFrame ) ): 
        if ( MeanShiftModel.labels_[j] != i ): 
            pixels[ int(dataFrame['x'][j]), int(dataFrame['y'][j]) ] = (255, 255, 255) 
    image.save( 'cluster' + str(i) + '.jpg' )

kMeansModel = KMeans(n_clusters=8) 
kMeansModel.fit( dataFrame ) 

for i in range( len( kMeansModel.cluster_centers_ ) ): 
    image = Image.open('destructuring.jpg') 
    pixels = image.load() 
    for j in range( len( dataFrame ) ): 
        if ( kMeansModel.labels_[j] != i ): 
            pixels[ int(dataFrame['x'][j]), int(dataFrame['y'][j]) ] = (255, 255, 255) 
        image.save( 'kmeanscluster' + str(i) + '.jpg' )