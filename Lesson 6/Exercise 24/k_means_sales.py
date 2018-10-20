import pandas 
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

dataFrame = pandas.read_csv('Sales_Transactions_Dataset_Weekly.csv')

dropColumns = ['Product_Code']
for w in range(0, 52): 
    dropColumns.append( 'W' + str(w) ) 
features = dataFrame.drop( dropColumns, 1) 

scaler = MinMaxScaler() 
scaledFeatures = scaler.fit_transform( features )

kMeansModel = KMeans() 
kMeansModel.fit( scaledFeatures )

print( 'Cluster centers: ', kMeansModel.cluster_centers_ )
print( '\n' )
print( 'Labels: ', kMeansModel.labels_ )