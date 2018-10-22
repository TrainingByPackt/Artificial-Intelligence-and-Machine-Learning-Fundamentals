

print('manual calculation')

TruePositives1 = 1  # both the predicted and test labels are true
FalsePositives1 = 0  # predicted label is true, test label is false
FalseNegatives1 = 3  # predicted label is false, test label is true
Precision1 = TruePositives1 / (TruePositives1 + FalsePositives1)
Recall1 = TruePositives1 / (TruePositives1 + FalseNegatives1)
F1_1 = 2*Precision1*Recall1 / (Precision1 + Recall1)
print('1st classifier (Precision, Recall, F1): ', Precision1, Recall1, F1_1)

TruePositives2 = 4
FalsePositives2 = 1
FalseNegatives2 = 0
Precision2 = TruePositives2 / (TruePositives2 + FalsePositives2)
Recall2 = TruePositives2 / (TruePositives2 + FalseNegatives2)
F1_2 = 2*Precision2*Recall2 / (Precision2 + Recall2)
print('2nd classifier (Precision, Recall, F1): ', Precision2, Recall2, F1_2)
