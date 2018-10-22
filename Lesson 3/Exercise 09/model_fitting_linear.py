import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn import model_selection

inputData = [2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62]
features = preprocessing.scale( inputData )
label = np.array(range(13))

( xTrain, xTest, yTrain, yTest ) = model_selection.train_test_split( features, label, test_size=0.1)

xTrain = xTrain.reshape(-1, 1)
xTest = xTest.reshape(-1, 1)

linearRegression = linear_model.LinearRegression()
model = linearRegression.fit( xTrain, yTrain )

print( 'yTest:' )
print( yTest )
print( '' )

print( 'y predicted:' )
print( model.predict( xTest ) )
print( '' )

print( 'model score:' )
print( model.score( xTest, yTest ) )
print( '' )
