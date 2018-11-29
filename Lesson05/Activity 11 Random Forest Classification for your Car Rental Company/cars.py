import pandas
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import classification_report
import numpy as np

# 1. Loading and preparing data for classification
data_frame = pandas.read_csv('car.data')

labels = {
    'Buying': ['vhigh', 'high', 'med', 'low'],
    'Maintenance': ['vhigh', 'high', 'med', 'low'],
    'Doors': ['2', '3', '4', '5more'],
    'Persons': ['2', '4', 'more'],
    'LuggageBoot': ['small', 'med', 'big'],
    'Safety': ['low', 'med', 'high'],
    'Class': ['unacc', 'acc', 'good', 'vgood']
}

label_encoders = {}
data_frame_encoded = pandas.DataFrame()
for column in data_frame:
    if column in labels:
        label_encoders[column] = preprocessing.LabelEncoder()
        label_encoders[column].fit(labels[column])
        data_frame_encoded[column] = label_encoders[column].transform(
            data_frame[column])
    else:
        data_frame_encoded[column] = data_frame[column]

features = np.array(data_frame_encoded.drop(['Class'], 1))
label = np.array(data_frame_encoded['Class'])

features_train, features_test, label_train, label_test = model_selection.train_test_split(
    features,
    label,
    test_size=0.1
)

# 2. Training the two classification models
random_forest_classifier = RandomForestClassifier(n_estimators=100, max_depth=6)
random_forest_classifier.fit(features_train, label_train)

extra_trees_classifier = ExtraTreesClassifier(n_estimators=100, max_depth=6)
extra_trees_classifier.fit(features_train, label_train)

# 3. Classification report for random forests and extremely random trees
print('random_forest_classifier:')
print(
    classification_report(
        label_test,
        random_forest_classifier.predict(features_test)
    )
)
print('\n\n')

print('extra_trees_classifier:')
print(
    classification_report(
        label_test,
        extra_trees_classifier.predict(features_test)
    )
)
print('\n')

print(
    'random_forest_classifier.feature_importances_: ',
    random_forest_classifier.feature_importances_
)
print('\n\n')

print(
    'extra_trees_classifier.feature_importances_: ',
    extra_trees_classifier.feature_importances_
)
print('\n\n')

# 4. Optimization via leaving out features
features2 = np.array(data_frame_encoded.drop(['Class', 'Doors'], 1))
label2 = np.array(data_frame_encoded['Class'])

features_train2, features_test2, label_train2, label_test2 = model_selection.train_test_split(
    features2,
    label2,
    test_size=0.1
)

random_forest_classifier2 = RandomForestClassifier(n_estimators=100, max_depth=6)
random_forest_classifier2.fit(features_train2, label_train2)

extra_trees_classifier2 = ExtraTreesClassifier(n_estimators=100, max_depth=6)
extra_trees_classifier2.fit(features_train2, label_train2)

print('random_forest_classifier2:')
print(
    classification_report(
        label_test2,
        random_forest_classifier2.predict(features_test2)
    )
)
print('\n\n')

print('extra_trees_classifier2:')
print(
    classification_report(
        label_test2,
        extra_trees_classifier2.predict(features_test2)
    )
)
print('\n\n')

# 5. Optimization via parametrization
random_forest_classifier3 = RandomForestClassifier(
    n_estimators=150, max_depth=8, criterion='entropy', max_features=5)
random_forest_classifier3.fit(features_train2, label_train2)

print('random_forest_classifier3:')
print(
    classification_report(
        label_test2,
        random_forest_classifier3.predict(features_test2)
    )
)
print('\n\n')

extra_trees_classifier3 = ExtraTreesClassifier(
    n_estimators=150, max_depth=8, criterion='entropy', max_features=5)


extra_trees_classifier3.fit(features_train2, label_train2)

print('extra_trees_classifier3:')
print(
    classification_report(
        label_test2,
        extra_trees_classifier3.predict(features_test2)
    )
)
