employees = [
 [20, 50000, 0],
 [24, 45000, 0],
 [32, 48000, 0],
 [24, 55000, 0],
 [40, 50000, 0],
 [40, 62000, 1],
 [40, 48000, 1],
 [32, 55000, 1],
 [40, 72000, 1],
 [32, 60000, 1]
]
scaled_employees = preprocessing.MinmaxScaler(
feature_range=(0,1)).fi_transform(employees)
import matplotlib.pyplot as plot
[
 plot.scatter(x[0], x[1], color = 'g' if x[2] > 0.5 else 'r')
 for x in scaled_employees
] + [plot.scatter(0.5, 0.25925925925925924, color='b')]