# creaye a list , print it , convert list to series and then print the series , create a homogenious array and then check the types

import pandas as pd
import numpy as np


num = [1, 2, 3, 4, 5]
print("List:", num)

s = pd.Series(num)


print("Series:\n", s)
print("Type of Series:", type(s))

homogeneous_array = np.array([10, 20, 30, 40, 50])


print("Homogeneous Array:", homogeneous_array)
print("Type of Homogeneous Array:", type(homogeneous_array))