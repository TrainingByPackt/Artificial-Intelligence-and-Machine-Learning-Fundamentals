import pandas
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

data_frame = pandas.read_csv('Sales_Transactions_Dataset_Weekly.csv')

drop_columns = ['Product_Code']
for w in range(0, 52):
    drop_columns.append('W' + str(w))
features = data_frame.drop(drop_columns, 1)

scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(features)

k_means_model = KMeans()
k_means_model.fit(scaled_features)

print('Cluster centers: ', k_means_model.cluster_centers_)
print('\n')
print('Labels: ', k_means_model.labels_)
