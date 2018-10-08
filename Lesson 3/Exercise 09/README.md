# Linear Regression with One Variable - Model fitting

## Exercise 1: Fibonacci

Perform model fitting splitting on the input data, where the features are scaled fibonacci values, and labels are their corresponding indices. Use the results of the previous exercise.

- Predict the test label values using your linear model
- Determine the model score

Input:

```
import numpy as np
from sklearn import preprocessing

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
features = preprocessing.scale( fibonacci )
label = np.array(range(13))

( xTrain, xTest, yTrain, yTest ) = model_selection.train_test_split( features, label, test_size=0.1)
```

Use Linear Regression provided by Scikit-learn:

```
from sklearn import linear_model
```

Solution: `model_fitting_fib.py`



## Exercise 2: Linear input


Replace the `fibonacci` array with the below `input`. Go through all the steps of the exercise.

```
inputData = [2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62]
```

Solution: `model_fitting_linear.py`


## Exercise 3: Calculate the best fit line manually

Use the input data from the second example, and use the `mean` function of the `numpy` library to calculate the slope and the constant coefficient of the best fit line.

```
import numpy as np
from numpy import mean
x = np.array(range(1, 14))
y = np.array([2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62])
```

Find the coefficients `a` and `b` from the `y = a*x + b` line.

Then use the following code to plot the results:

```
import matplotlib.pyplot as plot

plot.scatter( x, y )
plot.plot( [0, 15], [b, 15*a+b] )
```

Solution: `model_fitting_best_fit_line.py`


## Exercise 4: Calculate the best fit line with NumPy Polyfit

Use NumPy Polyfit to calculate the best fit line belonging to the following input:

```
import numpy as np 

x = np.array(range(1, 14)) 
y = np.array([2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62])
```

Solution: `model_fitting_np_polyfit.py`