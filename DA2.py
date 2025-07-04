import numpy as np

array1 = np.array([1,3,5,7,9,11])

array2 = np.reshape(array1,(2,3))

array3 = np.transpose(array2)

print("Original array:\n" , array1)
print("\nReshaped array:\n" , array2)
print("\nTransposed array:\n" , array3)