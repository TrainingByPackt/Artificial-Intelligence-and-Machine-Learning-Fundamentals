import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn import model_selection

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
features = preprocessing.scale(fibonacci)
label = np.array(range(13))

(x_train, x_test, y_train, y_test) = model_selection.train_test_split(
    features, label, test_size=0.1)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

linear_regression = linear_model.LinearRegression()
model = linear_regression.fit(x_train, y_train)

print('y_test:')
print(y_test)
print('')

print('y predicted:')
print(model.predict(x_test))
print('')

print('model score:')
print(model.score(x_test, y_test))
print('')
