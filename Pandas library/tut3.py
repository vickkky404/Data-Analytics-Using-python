import pandas as pd

my_list = [5,3,4,2,1]
# create a pandas Series from the list
s = pd.Series(my_list)
print(s)
print(type(s))
# create a numpy array from the list
import numpy as np
arr = np.array(my_list)
print(arr)
print(type(arr))