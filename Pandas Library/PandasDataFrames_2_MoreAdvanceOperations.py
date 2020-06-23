'''
This script elaborates more advanced operations on DataFrames.
'''

import pandas as pnd
import numpy as npy

# Create a DataFrame:
dict = {'Col1': [0, 0, 1, 0, 1, 1], 'Col2': ['A', 'B', 'C', 'D', 'E', 'F'],
        'Col3': npy.random.randint(1,10,6)}

dFrame = pnd.DataFrame(dict)
print('The DataFrame is: \n', dFrame)

## 1. SOME USEFUL FUNCTIONS ON THE DATAFRAMES ##
print('\n1. Some useful functions on the DataFrames \n')

# .groupby() funtion:
# The .groupby() creates a DataFrameGroupBy object. It groups the rows of the DataFrame based on a column.
groupedFrame = dFrame.groupby('Col1')
print(groupedFrame,'\n')

# .describe() function:
# .describe() function summarizes statistical features of the numerical columns of the DataFrame.
print(groupedFrame.describe(),'\n')

# It is also possible to get individual features:
print('The max for each group is: \n', groupedFrame.max(),'\n')
print('The min for each group is: \n', groupedFrame.min(),'\n')
print('The std for the numerical groups are: \n', groupedFrame.std(),'\n')
print('The number of elements in each group is: \n', groupedFrame.count(),'\n')

# .apply() function:
# Mapping functions to a column of a DataFrame
# Create a function:
def Cube(number):
    return number**3

cubeCol3 = dFrame['Col3'].apply(Cube) # This will calculate cube of every number in column 3
print(cubeCol3,'\n')

# .sort_values() function:
# It will sort the based on the column given as an input
print(dFrame.sort_values(by = 'Col3'),'\n')

# ----------------------------------- #
## 2. WORKING WITH MISSING DATA ON THE DATAFRAMES ##
print('\n2. Working with missing data on the DataFrames \n')

# Create a new DataFrame:
list = [[1, 2, 3], [npy.nan, 5, 6], ['D', 'E', npy.nan], ['E', 'D', npy.nan], [npy.nan, npy.nan, npy.nan]]
colLabels = ['Col1', 'Col2', 'Col3']

dFrame2 = pnd.DataFrame(data = list, columns = colLabels)
print('The new DataFrame is: \n', dFrame2)

# The "NaN" elements can be replaced by a new data using .fillna() function:
filledDFrame = dFrame2.fillna(value = 'DATA')
print('The filled DataFrame is: \n', filledDFrame)

# The rows with "NaN" elements can be dropped by using .dropna() function:
droppedDFrame = dFrame2.dropna()
print('The rows with "NaN"s have been dropped in the following DataFrame: \n', droppedDFrame)

# The rows with "NaN" elements can be dropped by using .dropna() based on a threshold value:
droppedDFrame2 = dFrame2.dropna(thresh = 2) # This will drop the rows having two or more "NaN"s
print('The rows with two or more "NaN"s have been dropped in the following DataFrame: \n', droppedDFrame2)

# ----------------------------------- #
## 3. COMBINING DATAFRAMES (Concatination/Merge/Join) ##
print('\n3. Combining DataFrames (Concatenation/Merge/Join) \n')

# Create new DataFrames:
dict1 = {'Col1': [11, 12, 13, 14], 'Col2': [21, 22, 23, 24],
        'Col3': [31, 32, 33, 34]}
dict2 = {'Col1': ['A1', 'A2', 'A3', 'A4'], 'Col2': ['B1', 'B2', 'B3', 'B4'],
        'Col3': ['C1', 'C2', 'C3', 'C4']}

dFr1 = pnd.DataFrame(dict1)
dFr2 = pnd.DataFrame(dict2)
print('The dFr1 is: \n', dFr1)
print('The dFr2 is: \n', dFr2)


# The new DataFrames can be concatenated using .concat() function. By default "axis = 0", so it will concat dFr2 below dFr1:
concatDFrame = pnd.concat([dFr1, dFr2])
print('The row concatenated DataFrame is: \n', concatDFrame)

# To concat dFr2 as new columns use "axis = 1". If the number of rows are not equal in the DataFrames,
# then it will fill the gaps by "NaN"s.
concatDFrame = pnd.concat([dFr1, dFr2, dFrame], axis = 1)
print('The column concatenated DataFrame is: \n', concatDFrame)

# The DataFrames can be joined using .join() function:
# The join operation can be done as "inner join" or "outer join".
# This is useful when the columns of two DataFrames with different row labels wants to be joined
dict3 = {'Col4': [1,2,3,4], 'Col5': [5,6,7,8], 'Col6': [9,0,1,2]}
dFr3 = pnd.DataFrame(dict3, index = [0, 1, 3, 4])
joinedDFrame = dFr1.join(dFr3, how = 'inner')
print('The inner joined DataFrame is: \n', joinedDFrame)
joinedDFrame2 = dFr1.join(dFr3, how = 'outer')
print('The outer joined DataFrame is: \n', joinedDFrame2)

# The DataFrames can be merged using .merge() function:
# This will merge two DataFrames on a common key
# It is possible to perform inner and outer merge similar to .join() function
dict4 = {'Col3': [31,32,35,34], 'Col5': [5,6,7,8], 'Col6': [9,0,1,2]}
dFr4 = pnd.DataFrame(dict4, index = [0, 1, 3, 4])
mergedDFrame = pnd.merge(dFr1, dFr4, on = 'Col3')
print('The merged DataFrame is: \n', mergedDFrame)