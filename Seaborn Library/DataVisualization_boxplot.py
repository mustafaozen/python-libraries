'''
This script exemplifies usage of Seaborn Library boxplot.
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

# Lets see distribution of sepal_width for each species using the boxplot:
plt.figure(1)
sb.boxplot(x = 'species', y = 'sepal_width', data = IrisData)

# The orientation of the figure can be changed:
plt.figure(2)
sb.boxplot(y = 'species', x = 'sepal_width', data = IrisData, orient = 'h')

plt.show()