import pandas 
import numpy as np 
from sklearn import model_selection 
from sklearn import preprocessing 
from sklearn import svm 

# 1. Loading data
dataFrame = pandas.read_csv('german.data', sep=' ')  
dataFrame.replace( 'NA', -1000000, inplace=True )

# 2. Label encoding
labels = { 
    'CheckingAccountStatus': ['A11', 'A12', 'A13', 'A14'], 
    'CreditHistory': ['A30', 'A31', 'A32', 'A33', 'A34'], 
    'CreditPurpose': ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410'], 
    'SavingsAccount': ['A61', 'A62', 'A63', 'A64', 'A65'], 
    'EmploymentSince': ['A71', 'A72', 'A73', 'A74', 'A75'], 
    'PersonalStatusSex': ['A91', 'A92', 'A93', 'A94', 'A95'],  
    'OtherDebtors': ['A101', 'A102', 'A103'],  
    'Property': ['A121', 'A122', 'A123', 'A124'], 
    'OtherInstallmentPlans': ['A141', 'A142', 'A143'], 
    'Housing': ['A151', 'A152', 'A153'], 
    'Job': ['A171', 'A172', 'A173', 'A174'], 
    'Phone': ['A191', 'A192'], 
    'ForeignWorker': ['A201', 'A202'] 
} 
labelEncoders = {} 
dataFrameEncoded = pandas.DataFrame() 

for column in dataFrame: 
    if column in labels: 
        labelEncoders[column] = preprocessing.LabelEncoder() 
        labelEncoders[column].fit( labels[column] ) 
        dataFrameEncoded[column] = labelEncoders[column].transform( dataFrame[column] ) 
    else: 
        dataFrameEncoded[column] = dataFrame[column] 


# 3. Identification of features and labels
features = np.array( dataFrameEncoded.drop(['CreditScore'], 1)) 
label = np.array( dataFrameEncoded['CreditScore'] )

# 4. Scaling features
scaledFeatures = preprocessing.MinMaxScaler( feature_range=(0,1) ).fit_transform( features )

# 5. Splitting training and testing data
featuresTrain, featuresTest, labelTrain, labelTest = model_selection.train_test_split( 
    scaledFeatures, 
    label, 
    test_size=0.2 
)

# 6. Classification
classifier = svm.SVC() 
# alternative parametrization:
# classifier = svm.SVC(kernel="poly", C=2, degree=4, gamma=0.05)

classifier.fit( featuresTrain, labelTrain )

print( 'Model score: ', classifier.score( featuresTest, labelTest ) )
