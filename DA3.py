import numpy as np

marks = np.array([76,78,81,66,85])

mean_marks = np.mean(marks)
print("Mean:" , mean_marks)

median_marks = np.min(marks)
print("Median: " , median_marks)

min_marks = np.min(marks)
print("Minimum marks: " , min_marks)

max_marks = np.max(marks)
print("Maximum mark: " , max_marks)