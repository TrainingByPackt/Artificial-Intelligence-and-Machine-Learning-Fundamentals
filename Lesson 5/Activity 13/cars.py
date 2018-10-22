import pandas
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import numpy as np

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

decisionTree = DecisionTreeClassifier()
decisionTree.fit(featuresTrain, labelTrain)

print('Score: ', decisionTree.score(featuresTest, labelTest))
print('\n\n')
print(
    classification_report(
        labelTest,
        decisionTree.predict(featuresTest)
    )
)
