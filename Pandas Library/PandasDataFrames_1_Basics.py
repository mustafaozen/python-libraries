'''
Introduction to Pandas' DataFrames.
This script provides simple examples on how to create and edit DataFrames.
For more details: https://pandas.pydata.org/pandas-docs/stable/index.html
'''

import pandas as pnd
import numpy as npy

npy.random.seed(101) # This command makes sure that the same random numbers are generated in each run

## 1. CREATING A DATAFRAME ##
# The DataFrames can be read from a file as well using pnd.read_csv(), etc. functions.
# Below, you can see how to create a DataFrame manually.
print('1. Creating a DataFrame\n')

# Approach 1:
rowIndex = ['Row1', 'Row2', 'Row3', 'Row4'] # labels of the rows of the DataFrame
colLabel = ['Col1', 'Col2', 'Col3', 'Col4'] # labels of the columns of the DataFrame
array = npy.random.randn(4,4)

dFrame1 = pnd.DataFrame(data = array, index = rowIndex, columns = colLabel)

print('The first dataframe: \n')
print(dFrame1)

# Another way:
dFrame2 = pnd.DataFrame(data = array, index = ['Row1', 'Row2', 'Row3', 'Row4'], columns = ['Col1', 'Col2', 'Col3', 'Col4'])

print('The second dataframe: \n')
print(dFrame2)

# Another way:
dFrame3 = pnd.DataFrame(data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], index = 'Row1 Row2 Row3'.split(), columns = 'Col1 Col2 Col3 Col4'.split())

print('The third dataframe: \n')
print(dFrame3)

# Another way: Using dictionaries
dict = {'Col1': [1, 2, 3, 4], 'Col2': [4, 3, 2, 1], 'Col3': [1, 1, 1, 1], 'Col4': npy.zeros(4)}
dFrame4 = pnd.DataFrame(dict)

print('The fourth dataframe: \n')
print(dFrame4)

# -------------------------------------- #
## 2. READING DATA FROM THE DATAFRAME ##
print('\n2. Reading data from the DataFrame \n')

# Reading one column of the DataFrame:
oneColumn = dFrame1['Col1']
print(oneColumn,'\n')

# Reading two columns of the DataFrame:
twoColumns = dFrame1[['Col1', 'Col2']]
print(twoColumns,'\n')

# Reading two columns of the DataFrame using indices:
twoColumns = dFrame1[1:3]
print(twoColumns,'\n')

# Reading one row of the DataFrame:
oneRow = dFrame1.loc['Row1']
print(oneRow,'\n')

# Reading two rows of the DataFrame:
twoRows = dFrame1.loc[['Row1', 'Row3']]
print(twoRows,'\n')

# Reading two rows of the DataFrame using integer location (Row1 --> 0, ..., Row4 --> 3):
twoRows2 = dFrame1.iloc[1:3]
print(twoRows2,'\n')

# -------------------------------------- #
## 3. ADDING A NEW COLUMN OR ROW TO THE DATAFRAME ##
print('\n3. Adding a new column or row to the DataFrame \n')

# Adding new columns:
dFrame1['Col5'] = npy.random.randn(4,1) # using numpy array
dFrame1['Col6'] = [6, 6, 6, 6] # using list
dFrame1['Col7'] = dFrame1['Col1'] + dFrame1['Col4'] # combining two column values into a new column
print('dFrame1 = \n', dFrame1,'\n')

# Adding new rows:
dFrame1.loc['Row5'] = npy.random.randn(7)
dFrame1.loc['Row6'] = [6, 6, 6, 6, 6, 6, 6]
dFrame1.loc['Row7'] = dFrame1.loc['Row1'] + dFrame1.loc['Row4']
print('dFrame1 = \n', dFrame1,'\n')

# -------------------------------------- #
## 4. DROPPING A COLUMN OR ROW FROM THE DATAFRAME ##
print('\n4. Dropping a column or row from the DataFrame \n')

# To drop a column, we need to specify column label and also set "axis = 1" to specify we are dropping a column
# "axis = 0" is used to drop a row.
# This following command outputs a DataFrame without Col7, but it actually doesn't drop Col7 from dFrame1:
dFrame1.drop('Col7', axis = 1)
print('dFrame1 = \n', dFrame1,'\n')

dfNew = dFrame1.drop('Col7', axis = 1)
print('dfNew = \n', dfNew,'\n')

# If we want to completely drop a column from the DataFrame itself, then set "inplace = True":
dFrame1.drop('Col7', axis = 1, inplace = True)
dFrame1.drop('Col6', axis = 1, inplace = True)
dFrame1.drop('Col5', axis = 1, inplace = True)
print('dFrame1 = \n', dFrame1,'\n')

# Removing rows inplace:
dFrame1.drop('Row7', axis = 0, inplace = True)
dFrame1.drop('Row6', axis = 0, inplace = True)
dFrame1.drop('Row5', axis = 0, inplace = True)
print('dFrame1 = \n', dFrame1,'\n')

# -------------------------------------- #
## 5. SELECTING ELEMENTS BASED ON CONDITIONS ##
print('\n5. Selecting elements based on conditions \n')

# Select rows where Col3 elements are negative:
print(dFrame1[dFrame1['Col3'] < 0], '\n')

# Select rows where Col1 and Col2 elements are positive:
print(dFrame1[(dFrame1['Col1'] > 0) & (dFrame1['Col2'] > 0)], '\n')

# Select rows where Col2 and Col4 elements less than or equal to 0.7:
print(dFrame1[(dFrame1.Col2 <= 0.7) & (dFrame1.Col4 <= 0.7)], '\n')

# -------------------------------------- #
## 6. SET/RESET/ADJUST DATAFRAME ROW LABELS ##
print('\n6. Set/Reset/Adjust DataFrame row labels \n')

# Resetting DataFrame row labels:
# This comment converts the initial row labels into a new column and adds new labels from 0 to number of rows - 1.
# If this is a permanent change, then use "dFrame.reset_index(inplace = True)"
print('dFrame1 = \n', dFrame1.reset_index(),'\n')

# Setting a column of the DataFrame as row labels:
dFrame1['Col1'] = [1, 2, 3, 4]
dFrame1.set_index('Col1', inplace = True)
print('dFrame1 = \n', dFrame1,'\n')

# Setting multilayer indices to a DataFrame:
colLabel = ['C1', 'C2', 'C3', 'C4']
outerLabel = ['Row1','Row1','Row2','Row2']
innerLabel = [1,2,1,2]
multiLayerLabel = pnd.MultiIndex.from_tuples(list(zip(outerLabel,innerLabel)))
dFrame1 = pnd.DataFrame(data = npy.random.randn(4,4), index = multiLayerLabel, columns = colLabel)
print('dFrame1 = \n', dFrame1,'\n')

# Read data from a DataFrame with multilayer labels:
print('dFrame1 = \n', dFrame1.loc['Row1']['C2'],'\n') # Column 2 of Row 1
print('dFrame1 = \n', dFrame1.loc['Row2'].loc[2],'\n') # Second row of Row2