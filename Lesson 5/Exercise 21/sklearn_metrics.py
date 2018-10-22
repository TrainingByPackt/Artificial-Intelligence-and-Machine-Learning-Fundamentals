from sklearn.metrics import classification_report
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score


TestLabels1 = [True, True, False, True, True]
PredictedLabels1 = [True, False, False, False, False]

TestLabels2 = [True, True, False, True, True]
PredictedLabels2 = [True, True, True, True, True]

print(
    'Precision1 (average=None, average=weighted)',
    precision_score(TestLabels1, PredictedLabels1, average=None),
    precision_score(TestLabels1, PredictedLabels1, average='weighted')
)
print('\n')

print(
    'Precision2 (average=None, average=weighted)',
    precision_score(TestLabels2, PredictedLabels2, average=None),
    precision_score(TestLabels2, PredictedLabels2, average='weighted')
)
print('\n')

print(
    'Recall1 (average=None, average=weighted)',
    recall_score(TestLabels1, PredictedLabels1, average=None),
    recall_score(TestLabels1, PredictedLabels1, average='weighted')
)
print('\n')

print(
    'Recall2 (average=None, average=weighted)',
    recall_score(TestLabels2, PredictedLabels2, average=None),
    recall_score(TestLabels2, PredictedLabels2, average='weighted')
)
print('\n')

print(
    'F1 Score 1 (average=None, average=weighted)',
    f1_score(TestLabels1, PredictedLabels1, average=None),
    f1_score(TestLabels1, PredictedLabels1, average='weighted')
)
print('\n')

print(
    'F1 Score 2 (average=None, average=weighted)',
    f1_score(TestLabels2, PredictedLabels2, average=None),
    f1_score(TestLabels2, PredictedLabels2, average='weighted')
)
print('\n')

print(
    'Accuracy Score 1',
    f1_score(TestLabels1, PredictedLabels1)
)
print('\n')

print(
    'Accuracy Score 2',
    f1_score(TestLabels2, PredictedLabels2)
)
print('\n\n')

print(
    classification_report(
        TestLabels1,
        PredictedLabels1
    )
)
print('\n\n')

print(
    classification_report(
        TestLabels2,
        PredictedLabels2
    )
)
