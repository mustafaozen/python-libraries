'''
This script exemplifies usage of Seaborn Library heatmap figures.
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

# Lets see the correlation between the features using the heatmap figure:
plt.figure(1,figsize = (12,10))
sb.heatmap(IrisData.corr())

# We can customize the figure:
plt.figure(2,figsize = (12,10))
sb.heatmap(IrisData.corr(), annot = True, cmap = 'YlGnBu')

plt.show()