'''
This script exemplifies K-Means Clustering using Python scikit-learn library.
For more details, see: https://scikit-learn.org/stable/
'''

from sklearn import datasets, cluster

import pandas as pnd
import numpy as npy
import matplotlib.pyplot as plt

# K-Means is a un-supervised learning, clustering algorithm. However, we treat iris data set as an un-supervised
# learning data set to exemplify this algorithm.
iris_data = datasets.load_iris() # Returns a dictionary

print(iris_data.keys())
print(iris_data.feature_names)

data = pnd.DataFrame(data = iris_data.data, columns = iris_data.feature_names)
print(data.head())

# The features are: sepal_length, sepal_width, petal_length, and petal_width.
# Using these features, we would like to predict if they are Setosa, Versicolour, Virginica
# Details on data set is available here: https://scikit-learn.org/stable/datasets/index.html


# We use two columns of data set we have for clustering.
X = data[['sepal length (cm)', 'petal length (cm)']]

# Initial figure for the data set:
plt.figure(1)
plt.scatter(x = X['sepal length (cm)'], y = X['petal length (cm)'])
plt.title('The data set')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')

# Creating the model and fitting it to the training data:
k_means = cluster.KMeans(n_clusters = 3) # We know that iris data set has 3 classes. That's why we can set n_cluster = 3.
# However, if you have no idea about the data set you are using, you can choose an appropriate n_cluster
# by minimizing sum of squared error or another criteria.
k_means.fit(X)

# Evaluation of the algorithm:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8,6))
ax1.set_title('True Labels')
ax1.scatter(X['sepal length (cm)'], X['petal length (cm)'], c = iris_data['target'], cmap = 'coolwarm')

ax2.set_title("K-Means")
ax2.scatter(X['sepal length (cm)'], X['petal length (cm)'], c = k_means.labels_, cmap = 'Accent')
plt.show()