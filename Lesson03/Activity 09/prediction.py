import quandl
import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plot
from sklearn import svm

data_frame = quandl.get("YALE/SPCOMP")
data_frame[['Long Interest Rate', 'Real Price',
           'Real Dividend', 'Cyclically Adjusted PE Ratio']]
data_frame.fillna(-100, inplace=True)

# We shift the price data to be predicted 20 years forward
data_frame['Real Price Label'] = data_frame['Real Price'].shift(-240)

# Then exclude the label column from the features
features = np.array(data_frame.drop('Real Price Label', 1))

# We scale before dropping the last 240 rows from the features
scaled_features = preprocessing.scale(features)

# Save the last 240 rows before dropping them
scaled_features_latest240 = scaled_features[-240:]

# Exclude the last 240 rows from the data used for model building
scaled_features = scaled_features[:-240]

# Now we can drop the last 240 rows from the data frame
data_frame.dropna(inplace=True)

# Then build the labels from the remaining data
label = np.array(data_frame['Real Price Label'])

# The rest of the model building stays
(features_train, features_test, label_train,
 label_test) = model_selection.train_test_split(scaled_features, label, test_size=0.1)

# Step 2:
#
# Linear model
model = linear_model.LinearRegression()
model.fit(features_train, label_train)
print('Linear model score: ', model.score(features_test, label_test))
print('\n')

label_predicted = model.predict(features_test)
plot.plot(
    label_test, label_predicted, 'o',
    [0, 3000], [0, 3000]
)


# Step 3:
#
# Polynomial model
poly_regressor = PolynomialFeatures(degree=3)
poly_scaled_features = poly_regressor.fit_transform(scaled_features)
(poly_features_train, poly_features_test, poly_label_train,
 poly_label_test) = model_selection.train_test_split(poly_scaled_features, label, test_size=0.1)
model = linear_model.LinearRegression()
model.fit(poly_features_train, poly_label_train)

print('Polynomial model score: ', model.score(
    poly_features_test, poly_label_test))
print('\n')

poly_label_predicted = model.predict(poly_features_test)
plot.plot(
    poly_label_test, poly_label_predicted, 'o',
    [0, 3000], [0, 3000]
)


# Step 4:
#
# Support Vector Regression
model = svm.SVR(kernel='poly')
model.fit(features_train, label_train)
print('SVM model score: ', model.score(features_test, label_test))
label_predicted = model.predict(features_test)
plot.plot(
    label_test, label_predicted, 'o',
    [0, 3000], [0, 3000]
)
