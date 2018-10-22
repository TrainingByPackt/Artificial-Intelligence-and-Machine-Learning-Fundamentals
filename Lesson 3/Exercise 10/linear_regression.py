import numpy as np
import quandl
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plot

dataFrame = quandl.get("YALE/SPCOMP")

dataFrame.fillna(-100, inplace=True)

dataFrame['Real Price Label'] = dataFrame['Real Price'].shift(-240)

dataFrame.dropna(inplace=True)

features = np.array(dataFrame.drop('Real Price Label', 1))
label = np.array(dataFrame['Real Price Label'])

scaledFeatures = preprocessing.scale(features)

(featuresTrain, featuresTest, labelTrain,
 labelTest) = model_selection.train_test_split(scaledFeatures, label, test_size=0.1)

model = linear_model.LinearRegression()
model.fit(featuresTrain, labelTrain)

labelPredicted = model.predict(featuresTest)

print('Model score: ', model.score(featuresTest, labelTest))

plot.scatter(labelTest, labelPredicted)
