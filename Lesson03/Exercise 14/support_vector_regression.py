import numpy as np
import quandl
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import svm
from matplotlib import pyplot as plot

data_frame = quandl.get("YALE/SPCOMP")

data_frame.fillna(-100, inplace=True)

# We shift the price data to be predicted 20 years forward
data_frame['Real Price Label'] = data_frame['Real Price'].shift(-240)

# Then exclude the label column from the features
features = np.array(data_frame.drop('Real Price Label', 1))

# We scale before dropping the last 240 rows from the features
scaled_features = preprocessing.scale(features)

# Save the last 240 rows before dropping them
scaled_features_latest_240 = scaled_features[-240:]

# Exclude the last 240 rows from the data used for model building
scaled_features = scaled_features[:-240]

# Now we can drop the last 240 rows from the data frame
data_frame.dropna(inplace=True)

# Then build the labels from the remaining data
label = np.array(data_frame['Real Price Label'])

# The rest of the model building stays the same
(features_train, features_test, label_train,
 label_test) = model_selection.train_test_split(scaled_features, label, test_size=0.1)

model = svm.SVR()
model.fit(features_train, label_train)

label_predicted = model.predict(features_test)

print('Score: ', model.score(features_test, label_test))

plot.plot(label_test, label_predicted, 'o')
