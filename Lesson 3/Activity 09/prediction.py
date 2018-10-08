import quandl 
import numpy as np 
from sklearn import preprocessing 
from sklearn import model_selection 
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plot 

dataFrame = quandl.get("YALE/SPCOMP") 
dataFrame[['Long Interest Rate', 'Real Price', 'Real Dividend', 'Cyclically Adjusted PE Ratio']] 
dataFrame.fillna(-100, inplace=True) 

# We shift the price data to be predicted 20 years forward 
dataFrame[ 'Real Price Label'] = dataFrame[ 'Real Price'].shift( -240 ) 

# Then exclude the label column from the features 
features = np.array( dataFrame.drop('Real Price Label', 1) ) 

# We scale before dropping the last 240 rows from the features 
scaledFeatures = preprocessing.scale( features ) 

# Save the last 240 rows before dropping them 
scaledFeaturesLatest240 = scaledFeatures[-240:]  

# Exclude the last 240 rows from the data used for model building 
scaledFeatures = scaledFeatures[:-240] 

# Now we can drop the last 240 rows from the data frame 
dataFrame.dropna(inplace=True) 

# Then build the labels from the remaining data 
label = np.array( dataFrame['Real Price Label'] ) 

# The rest of the model building stays 
(featuresTrain, featuresTest, labelTrain, labelTest) = model_selection.train_test_split( scaledFeatures, label, test_size=0.1)

# Step 2:
#
# Linear model
model = linear_model.LinearRegression() 
model.fit( featuresTrain, labelTrain ) 
print( 'Linear model score: ', model.score( featuresTest, labelTest ) )

labelPredicted = model.predict(featuresTest) 
plot.plot(  
    labelTest, labelPredicted, 'o', 
    [0,3000], [0,3000] 
)


# Step 3: 
#
# Polynomial model
polyRegressor = PolynomialFeatures(degree=3)
polyScaledFeatures = polyRegressor.fit_transform( scaledFeatures )
(polyFeaturesTrain, polyFeaturesTest, polyLabelTrain, polyLabelTest) = model_selection.train_test_split( polyScaledFeatures, label, test_size=0.1)
linearModel = linear_model.LinearRegression() 
linearModel.fit( polyFeaturesTrain, polyLabelTrain )

print( 'Polynomial model score: ', linearModel.score( polyFeaturesTest, polyLabelTest ) )

polyLabelPredicted = linearModel.predict(polyFeaturesTest) 
plot.plot(  
    polyLabelTest, polyLabelPredicted, 'o', 
    [0,3000], [0,3000] 
)


# Step 4: 
#
# Support Vector Regression
model = svm.SVR( kernel='poly' ) 
model.fit( featuresTrain, labelTrain ) 
print( 'SVM model score: ', model.score( featuresTest, labelTest ) )
labelPredicted = model.predict( featuresTest ) 
plot.plot(  
    labelTest, labelPredicted, 'o', 
    [0,3000], [0,3000] 
)
