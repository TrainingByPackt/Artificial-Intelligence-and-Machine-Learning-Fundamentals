import numpy as np 
import quandl 
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from matplotlib import pyplot as plot
from sklearn.preprocessing import PolynomialFeatures 

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

# Create a polynomial regressor model and fit it to the training data
polyRegressor = PolynomialFeatures(degree=3)
polyScaledFeatures = polyRegressor.fit_transform( scaledFeatures )

# Split to training and testing data
(polyFeaturesTrain, polyFeaturesTest, polyLabelTrain, polyLabelTest) = model_selection.train_test_split( polyScaledFeatures, label, test_size=0.1)

# Apply linear regression
linearModel = linear_model.LinearRegression() 
linearModel.fit( polyFeaturesTrain, polyLabelTrain )

# Model score
print( 'Score: ', linearModel.score(polyFeaturesTest, polyLabelTest) )

# Prediction
polyLabelPredicted = linearModel.predict( polyFeaturesTest )
plot.scatter( polyLabelTest, polyLabelPredicted)
