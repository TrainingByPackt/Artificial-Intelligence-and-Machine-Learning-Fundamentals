import numpy as np
import quandl
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plot
from sklearn.preprocessing import PolynomialFeatures

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

# Create a polynomial regressor model and fit it to the training data
poly_regressor = PolynomialFeatures(degree=3)
poly_scaled_features = poly_regressor.fit_transform(scaled_features)

# Split to training and testing data
(poly_features_train, poly_features_test, poly_label_train,
 poly_label_test) = model_selection.train_test_split(poly_scaled_features, label, test_size=0.1)

# Apply linear regression
model = linear_model.LinearRegression()
model.fit(poly_features_train, poly_label_train)

# Model score
print('Score: ', model.score(poly_features_test, poly_label_test))

# Prediction
poly_label_predicted = model.predict(poly_features_test)
plot.scatter(poly_label_test, poly_label_predicted)
