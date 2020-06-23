'''
This script exemplifies usage of Seaborn Library barplot.
For more details, see: https://seaborn.pydata.org/
'''

import seaborn as sb
import matplotlib.pyplot as plt
import numpy as npy

# Seaborn library has some example built-in data sets. You can use sb.get_dataset_names() to list the available data sets.
# Lets use one of them:
# The Iris data set is perhaps the best known data set used usually for exemplifying machine learning classification algorithms.

IrisData = sb.load_dataset('iris')
print(IrisData.head())
print(IrisData.describe())

# Lets see barplot with error bar(STDs) of species versus sepal_width:
plt.figure(1)
sb.barplot(x = 'species', y = 'sepal_width', data = IrisData, estimator = npy.std)


# We can customize the figure:
plt.figure(2)
sb.barplot(x = 'species', y = 'sepal_width', data = IrisData, palette = 'rainbow')

plt.show()