# Linear Regression with One Variable - Cross Validation

**Exercise:** Perform train-test splitting on the input data, where the features are scaled fibonacci values, and labels are their corresponding indices. Use 10% of the data as testing data.

```
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
features = preprocessing.scale( fibonacci )
label = np.array(range(13))
```

Solution: `cross_validation.py`


