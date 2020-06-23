'''
This script exemplifies usage of Seaborn Library countplot.
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

# Lets see the number of each specie in the data set using the countplot:
sb.countplot(x = 'species', data = IrisData)

plt.show()