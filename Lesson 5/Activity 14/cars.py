import pandas
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import classification_report
import numpy as np

# 1. Loading and preparing data for classification
dataFrame = pandas.read_csv('car.data')

labels = {
    'Buying': ['vhigh', 'high', 'med', 'low'],
    'Maintenance': ['vhigh', 'high', 'med', 'low'],
    'Doors': ['2', '3', '4', '5more'],
    'Persons': ['2', '4', 'more'],
    'LuggageBoot': ['small', 'med', 'big'],
    'Safety': ['low', 'med', 'high'],
    'Class': ['unacc', 'acc', 'good', 'vgood']
}

labelEncoders = {}
dataFrameEncoded = pandas.DataFrame()
for column in dataFrame:
    if column in labels:
        labelEncoders[column] = preprocessing.LabelEncoder()
        labelEncoders[column].fit(labels[column])
        dataFrameEncoded[column] = labelEncoders[column].transform(
            dataFrame[column])
    else:
        dataFrameEncoded[column] = dataFrame[column]

features = np.array(dataFrameEncoded.drop(['Class'], 1))
label = np.array(dataFrameEncoded['Class'])

featuresTrain, featuresTest, labelTrain, labelTest = model_selection.train_test_split(
    features,
    label,
    test_size=0.1
)

# 2. Training the two classification models
randomForestClassifier = RandomForestClassifier(n_estimators=100, max_depth=6)
randomForestClassifier.fit(featuresTrain, labelTrain)

extraTreesClassifier = ExtraTreesClassifier(n_estimators=100, max_depth=6)
extraTreesClassifier.fit(featuresTrain, labelTrain)

# 3. Classification report for random forests and extremely random trees
print('randomForestClassifier:')
print(
    classification_report(
        labelTest,
        randomForestClassifier.predict(featuresTest)
    )
)
print('\n\n')

print('extraTreesClassifier:')
print(
    classification_report(
        labelTest,
        extraTreesClassifier.predict(featuresTest)
    )
)
print('\n')

print(
    'randomForestClassifier.feature_importances_: ',
    randomForestClassifier.feature_importances_
)
print('\n\n')

print(
    'extraTreesClassifier.feature_importances_: ',
    extraTreesClassifier.feature_importances_
)
print('\n\n')

# 4. Optimization via leaving out features
features2 = np.array(dataFrameEncoded.drop(['Class', 'Doors'], 1))
label2 = np.array(dataFrameEncoded['Class'])

featuresTrain2, featuresTest2, labelTrain2, labelTest2 = model_selection.train_test_split(
    features2,
    label2,
    test_size=0.1
)

randomForestClassifier2 = RandomForestClassifier(n_estimators=100, max_depth=6)
randomForestClassifier2.fit(featuresTrain2, labelTrain2)

extraTreesClassifier2 = ExtraTreesClassifier(n_estimators=100, max_depth=6)
extraTreesClassifier2.fit(featuresTrain2, labelTrain2)

print('randomForestClassifier2:')
print(
    classification_report(
        labelTest2,
        randomForestClassifier2.predict(featuresTest2)
    )
)
print('\n\n')

print('extraTreesClassifier2:')
print(
    classification_report(
        labelTest2,
        extraTreesClassifier2.predict(featuresTest2)
    )
)
print('\n\n')

# 5. Optimization via parametrization
randomForestClassifier3 = RandomForestClassifier(
    n_estimators=150, max_depth=8, criterion='entropy', max_features=5)
randomForestClassifier3.fit(featuresTrain2, labelTrain2)

print('randomForestClassifier3:')
print(
    classification_report(
        labelTest2,
        randomForestClassifier3.predict(featuresTest2)
    )
)
print('\n\n')

extraTreesClassifier3 = ExtraTreesClassifier(
    n_estimators=150, max_depth=8, criterion='entropy', max_features=5)


extraTreesClassifier3.fit(featuresTrain2, labelTrain2)

print('extraTreesClassifier3:')
print(
    classification_report(
        labelTest2,
        extraTreesClassifier3.predict(featuresTest2)
    )
)
