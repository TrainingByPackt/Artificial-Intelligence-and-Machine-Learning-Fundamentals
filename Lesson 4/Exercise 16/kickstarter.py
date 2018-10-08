from sklearn import preprocessing
import numpy as np

dataFrame = pandas.read_csv('ks-projects-201801.csv', sep=',') 

​dataFrame.replace( 'NA', -1000000, inplace=True ) 
dataFrame.replace( 'N/A', -1000000, inplace=True )

dataFrame.drop( ['ID'], 1, inplace=True )

[dataFrame['backers']] = preprocessing.Binarizer(threshold=1).transform( [dataFrame['backers']] )

labels = ['AUD', 'CAD', 'CHF', 'DKK', 'EUR', 'GBP', 'HKD', 'JPY', 'MXN', 'NOK', 'NZD', 'SEK', 'SGD', 'USD'] 
labelEncoder = preprocessing.LabelEncoder() 
labelEncoder.fit( labels ) 
dataFrame['currency'] = labelEncoder.transform( dataFrame['currency'] )

valuesToScale = np.mat([dataFrame['goal']]).transpose() 
[dataFrame['goal']] = preprocessing.MinMaxScaler( feature_range=(0,1) ).fit_transform( valuesToScale ).transpose()

dataFrame.head()