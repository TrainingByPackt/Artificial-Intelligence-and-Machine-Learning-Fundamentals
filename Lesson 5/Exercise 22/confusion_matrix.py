from sklearn.metrics import confusion_matrix

TestLabels1 = [True, True, False, True, True]
PredictedLabels1 = [True, False, False, False, False]

TestLabels2 = [True, True, False, True, True]
PredictedLabels2 = [True, True, True, True, True]

print('Confusion Matrix 1', confusion_matrix(TestLabels1, PredictedLabels1))
print('Confusion Matrix 2', confusion_matrix(TestLabels2, PredictedLabels2))
