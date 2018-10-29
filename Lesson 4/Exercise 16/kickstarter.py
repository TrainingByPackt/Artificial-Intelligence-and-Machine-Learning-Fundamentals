from sklearn import preprocessing
import numpy as np
import pandas

data_frame = pandas.read_csv('ks-projects-201801.csv', sep=',')

data_frame.replace('NA', -1000000, inplace=True)
data_frame.replace('N/A', -1000000, inplace=True)

data_frame.drop(['ID'], 1, inplace=True)

[data_frame['backers']] = preprocessing.Binarizer(
    threshold=1).transform([data_frame['backers']])

labels = ['AUD', 'CAD', 'CHF', 'DKK', 'EUR', 'GBP', 'HKD',
          'JPY', 'MXN', 'NOK', 'NZD', 'SEK', 'SGD', 'USD']
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(labels)
data_frame['currency'] = label_encoder.transform(data_frame['currency'])

values_to_scale = np.mat([data_frame['goal']]).transpose()
[data_frame['goal']] = preprocessing.MinMaxScaler(
    feature_range=(0, 1)).fit_transform(values_to_scale).transpose()

data_frame.head()
