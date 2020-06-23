'''
This script exemplifies usage of Seaborn Library lmplot.
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

# lmplot is used for regression plot. It fits a liner line for the provided data:
sb.lmplot(x = 'sepal_length', y = 'petal_width', data = IrisData)

# We can distinguish the data using hue and fit a line for each species:
sb.lmplot(x = 'sepal_length', y = 'petal_width', data = IrisData, hue = 'species')

plt.show()