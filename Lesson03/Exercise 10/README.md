# Linear Regression with Multiple Variables

Install `quandl`:

```
pip install quandl
```

Get a data frame of the S&P 500:

```
import quandl 

data_frame = quandl.get("YALE/SPCOMP")
```

Perform the following steps:

0. Suppose a data frame is given with preloaded data 
1. Select the columns from the data set you are interested in 
2. Replace NaN values with a numeric value to avoid getting rid of data 
3. Determin the forecast interval T determining the amount of time or number of data rows you wish to look into the future.  
4. Create a label column out of the value you wish to forecast. For row i of the data frame, the value of the label should belong to the time instant i+T.  
5. For the last T rows, the label value is NaN. Drop these rows from the data frame 
6. Create NumPy arrays from the features and the label 
7. Scale the features array 
8. Separate training and testing data

File: `linear_regression.py`.