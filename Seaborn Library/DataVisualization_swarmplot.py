'''
This script exemplifies usage of Seaborn Library swarmplot.
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

# Lets see distribution of sepal_width for each species using the swarmplot:
plt.figure(1)
sb.swarmplot(x = 'species', y = 'sepal_width', data = IrisData)

# We can combine multiple visualization methods such as violinplot and swarmplot to better interpret data:
plt.figure(2)
sb.violinplot(x = 'species', y = 'sepal_width', data = IrisData)
sb.swarmplot(x = 'species', y = 'sepal_width', data = IrisData, color = 'black')

plt.show()