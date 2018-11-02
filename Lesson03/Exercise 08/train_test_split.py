import numpy as np
from sklearn import preprocessing
from sklearn import model_selection

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
features = preprocessing.scale(fibonacci)
label = np.array(range(13))

(x_train, x_test, y_train, y_test) = model_selection.train_test_split(
    features, label, test_size=0.1)

print('x_train:')
print(x_train)
print('')

print('x_test:')
print(x_test)
print('')

print('y_train:')
print(y_train)
print('')

print('y_test:')
print(y_test)
print('')
