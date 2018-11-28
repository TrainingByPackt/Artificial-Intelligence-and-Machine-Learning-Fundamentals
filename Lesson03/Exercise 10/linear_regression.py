import numpy as np
import quandl
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plot

data_frame = quandl.get("YALE/SPCOMP")

data_frame.fillna(-100, inplace=True)

data_frame['Real Price Label'] = data_frame['Real Price'].shift(-240)

data_frame.dropna(inplace=True)

features = np.array(data_frame.drop('Real Price Label', 1))
label = np.array(data_frame['Real Price Label'])

scaled_features = preprocessing.scale(features)

(features_train, features_test, label_train,
 label_test) = model_selection.train_test_split(scaled_features, label, test_size=0.1)

model = linear_model.LinearRegression()
model.fit(features_train, label_train)

label_predicted = model.predict(features_test)

print('Model score: ', model.score(features_test, label_test))

plot.scatter(label_test, label_predicted)
