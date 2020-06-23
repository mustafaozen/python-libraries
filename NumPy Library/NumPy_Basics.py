'''
Introduction to NumPy Library.
This script introduces how to create NumPy arrays and how to operate with them.
For more details: https://numpy.org/devdocs/user/quickstart.html
'''

import numpy as npy

## 1. CREATING NumPy ARRAYS ##

# Casting lists to arrays:
list = [1,2,3,4,5]

array1 = npy.array(list)
print('The array1 is: ', array1)

# Using NumPy built-in functions:

# .zeros() creates an array of 0s with user-defined dimensions.
array2 = npy.zeros((1,5)) # the input is a tuple.
print('\n The array2 is: ', array2)

# .ones() creates an array of 1s with user-defined dimensions.
array3 = npy.ones((2,3))
print('\n The array3 is: \n', array3)

# .eye() creates an identity matrix with user-defined dimensions.
array4 = npy.eye(5)
print('\n The array4 is: \n', array4)

# .arange() creates an array of evenly spaced values within the user-specified interval.
array5 = npy.arange(1,11)
print('\n The array5 is: \n', array5)

array6 = npy.arange(1,100, 10) # Starts from 1 and iterates by adding 10 until it reaches to the upper limit 100.
print('\n The array6 is: \n', array6)

# .linspace() creates an array of evenly spaced values.
array7 = npy.linspace(1,100, 10) # divides the interval 1 to 100 into 10 equivalent pieces.
print('\n The array7 is: \n', array7)

# .random.rand() can create an array with random number entries with user-defined dimension
array8 = npy.random.rand(2,3) # by default, the generated numbers are between 0 to 1.
print('\n The array8 is: \n', array8)

# similarly:
array9 = npy.random.randn(2,3) # the entries of the array are coming from Standard Normal Distribution.
print('\n The array9 is: \n', array9)

array10 = npy.random.randint(1,10, 15) # generates random integers within a given interval.
print('\n The array10 is: \n', array10)

# Reshaping the array:
newArray10 = array10.reshape(3,5) # make sure d1xd2 = initial length. In this example 3x5 = 15 matches array10 length
print('\n The newArray10 is: \n', newArray10)


## 2. BUILT-IN ARRAY ATTRIBUTES ##

# Generate an array with random integer values between 1 and 100:
array = npy.random.randint(1,100,10)
print('\n The array is: \n', array)

# Finding the maximum entry of the array
arrMax = array.max()
print('\n The maximum entry of array is: ', arrMax, '\n')

# Finding the minimum entry of the array
arrMin = array.min()
print('\n The minimum entry of array is: ', arrMin, '\n')

# Fining the index of the maximum and minimum entries:
arrMinInd = array.argmin()
print('\n The index of the minimum entry of array is: ', arrMinInd, '\n') # Remember, indexing starts from 0!

arrMaxInd = array.argmax()
print('\n The index of the maximum entry of array is: ', arrMaxInd, '\n')

# Finding length the array
lenArray = len(array)
print('\n The length of the array is: ', lenArray, '\n')

# Finding dimensions of an array
dimArray = array8.shape
print('\n The dimensions of the array8 is: ', dimArray, '\n')

## 3. ARRAY INDEXING AND ENTRY SELECTION ##

# Create a new array:
array = npy.arange(1,21).reshape(4,5)
print('\n The new array is: \n', array)

# Picking a single entry from the array:
anEntry = array[1, 3] # retrieving entry 9
print('\n The picked entry is: ', anEntry, '\n')

# Picking an entire row of the array:
aRow = array[1, :] # retrieving the 2nd row
print('\n The picked row is: ', aRow, '\n')

# Picking an entire column of the array:
aColumn = array[:, 4] # retrieving the 5th column
print('\n The picked column is: ', aColumn, '\n')

# Picking multiple rows and columns of the array:
multiRowColumn = array[0:2, 2:4] # retrieving the 1st and 2nd row, and 3rd,4th columns
print('\n The picked multiRowColumn are: \n', multiRowColumn, '\n')

# Picking rows irregularly:
irregRows = array[[1,3]] # retrieving the 1st and 3rd rows
print('\n The picked irregRows are: \n', irregRows, '\n')

## 4. ARRAY OPERATIONS ##

# Adding arrays
arrAdd = array + array
print('\n The arrAdd is: \n', arrAdd, '\n')

# Substituting arrays
arrSubs = array - array
print('\n The arrSubs is: \n', arrSubs, '\n')

# Multiplying arrays
arrMult = array * array
print('\n The arrMult is: \n', arrMult, '\n')

# Dividing arrays
arrDiv = array / array
print('\n The arrDiv is: \n', arrDiv, '\n')

# Power of arrays
arrPow = array**4
print('\n The arrPow is: \n', arrPow, '\n')

# Square root of entries of array
arrSqrt = npy.sqrt(array)
print('\n The arrSqrt is: \n', arrSqrt, '\n')

# Sine of entries of array
arrSin = npy.sin(array)
print('\n The arrSin is: \n', arrSin, '\n')

# Exponention of entries of array
arrExp = npy.exp(array)
print('\n The arrExp is: \n', arrExp, '\n')

# Logarithm of entries of array
arrLog = npy.log(array)
print('\n The arrLog is: \n', arrLog, '\n')