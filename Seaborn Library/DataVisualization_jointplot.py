'''
This script exemplifies usage of Seaborn Library jointplot.
For more details, see: https://seaborn.pydata.org/
'''

import seaborn as sb
import matplotlib.pyplot as plt

# Seaborn library has some example built-in data sets. You can use sb.get_dataset_names() to list the available data sets.
# Lets use one of them:
# The Iris data set is perhaps the best known data set used usually for exemplifying machine learning classification algorithms.

IrisData = sb.load_dataset('iris')
print(IrisData.head())
print(IrisData.describe())

# Lets see joint distribution of sepal length and sepal width:

sb.jointplot(x = 'sepal_length', y = 'sepal_width', data = IrisData, kind = 'scatter')


# The kind of the joint plot can be changed:
# Hex plot
sb.jointplot(x = IrisData['petal_length'], y = IrisData['petal_width'], kind = 'hex')


# Linear Regression: fits a liner line to the data
sb.jointplot(x = IrisData['petal_length'], y = IrisData['petal_width'], kind = 'reg')
plt.show()