'''
This script exemplifies usage of Seaborn Library distribution plot.
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

# Lets see how sepal length is distributed:

# .distplot(): by default creates the histogram plot of the given data including Kernel Density Estimation curve.
plt.figure(1)
sb.distplot(IrisData['sepal_length'],bins = 20)

# KDE can be turned of:
plt.figure(2)
sb.distplot(IrisData['sepal_length'],bins = 20, kde = False)
plt.show()