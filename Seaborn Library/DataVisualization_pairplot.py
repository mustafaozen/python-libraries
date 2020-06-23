'''
This script exemplifies usage of Seaborn Library pairplot.
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

# .pairplot(): good for pairwise comparison of the features in the data set
sb.pairplot(IrisData)


# We can pass a hue feature which color codes the data based on a feature:
sb.pairplot(IrisData, hue = 'species')
plt.show()

# Based on Figure 2, setosa can easily be distinguished from versicolor and virginica!