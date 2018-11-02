import pandas
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import numpy as np

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

decision_tree = DecisionTreeClassifier()
decision_tree.fit(features_train, label_train)

print('Score: ', decision_tree.score(features_test, label_test))
print('\n\n')
print(
    classification_report(
        label_test,
        decision_tree.predict(features_test)
    )
)
