from sklearn import preprocessing
import numpy as np
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Min-max scaling:
minmax = [(float(i)-min(fibonacci))/(max(fibonacci)-min(fibonacci))
          for i in fibonacci]
print('minmax:')
print(minmax)
print('')

# Mean normalization:
avg = sum(fibonacci) / len(fibonacci)
# 28.923076923076923
mean = [(float(i)-avg)/(max(fibonacci)-min(fibonacci)) for i in fibonacci]
print('mean:')
print(mean)
print('')

# sklearn:
skmean = preprocessing.scale(fibonacci)
print('skmean:')
print(skmean)
print('')
