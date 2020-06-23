'''
This script exemplifies usage of Seaborn Library kdeplot that is the Kernel Density estimation of a given data.
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

# Lets see kernel density estimation curve of sepal_width:
plt.figure(1)
sb.kdeplot(IrisData['sepal_width'])


# We can modify the figure as follows
plt.figure(2)
sb.kdeplot(IrisData['sepal_width'], shade = True, vertical = True, legend = False)


# We can make a 2D KED plot as well:
plt.figure(3)
sb.kdeplot(IrisData['sepal_width'], IrisData['sepal_length'], shade = True)
plt.show()
