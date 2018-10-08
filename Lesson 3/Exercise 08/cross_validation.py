from sklearn import model_selection

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
features = preprocessing.scale( fibonacci )
label = np.array(range(13))

( xTrain, xTest, yTrain, yTest ) = model_selection.train_test_split( features, label, test_size=0.1) 

print( 'xTrain:' )
print( xTrain )
print( '' )

print( 'xTest:' )
print( xTest )
print( '' )

print( 'yTrain:' )
print( yTrain )
print( '' )

print( 'yTest:' )
print( yTest )
print( '' )