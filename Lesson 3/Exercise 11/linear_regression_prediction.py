import numpy as np 
import quandl 
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plot

dataFrame = quandl.get("YALE/SPCOMP")

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

# The rest of the model building stays the same 
(featuresTrain, featuresTest, labelTrain, labelTest) = model_selection.train_test_split( scaledFeatures, label, test_size=0.1)

model = linear_model.LinearRegression() 
model.fit( featuresTrain, labelTrain )

labelPredicted = model.predict( scaledFeaturesLatest240 ) 

plot.plot( list(range(1,181)), labelPredicted[:180] )
