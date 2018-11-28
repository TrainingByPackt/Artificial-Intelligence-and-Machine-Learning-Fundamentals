# Polynomial regression with one variable

Perform 1st, 2nd, and 3rd degree polynomial regrssion on the following datasets:

```
import numpy as np 

# First dataset: 
x1 = np.array(range(1, 14)) 
y1 = np.array([2, 8, 8, 18, 25, 21, 32, 44, 32, 48, 61, 45, 62]) 

# Second dataset: 
x2 = np.array(range(1, 14)) 
​y2 = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
```

Call your polynomial approximation functions `f1`, `f2`, and `f3` respectively.

Plot your results using the following code:

```
# First dataset:
plot.plot( 
    x1, y1, 'o', 
    x1, f1(x1), 
    x1, f2(x1), 
    x1, f3(x1) 
​)

# Second dataset:
plot.plot( 
    x2, y1, 'o',# blue dots 
    x2, f1(x2), # orange 
    x2, f2(x2), # green 
    x2, f3(x2)  # red 
​)
```


Solutions:

- `first.py`
- `second.py`