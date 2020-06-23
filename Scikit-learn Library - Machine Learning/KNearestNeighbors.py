'''
This script exemplifies K Nearest Neighbors using Python scikit-learn library
For more details, see: https://scikit-learn.org/stable/
'''

from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import matplotlib.pyplot as plt
import pandas as pnd
import numpy as npy

# Lets use one of the built-in data set in scikit-learn library:
iris_data = datasets.load_iris() # Returns a dictionary

print(iris_data.keys())
print(iris_data.feature_names)

data = pnd.DataFrame(data = iris_data.data, columns = iris_data.feature_names)
data['target'] = iris_data['target']
print(data.head())

# The features are: sepal_length, sepal_width, petal_length, and petal_width.
# Using these features, we would like to predict if they are Setosa, Versicolour, Virginica
# Details on data set is available here: https://scikit-learn.org/stable/datasets/index.html


# Splitting the data set into training and testing data. 40% of the data is kept as testing data:
X = data.drop('target', axis = 1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# Creating the model and fitting it to the training data:
knn = neighbors.KNeighborsClassifier(n_neighbors = 3) # number of neighbours is important. Higher is better.
knn.fit(X_train, y_train)

# Testing the model:
predictions = knn.predict(X_test)
trainPredictions = knn.predict(X_train)

# Model evaluations:
print('Training report: \n', classification_report(y_train, trainPredictions))
print('Testing report: \n', classification_report(y_test, predictions))
print('Confusion Matrix is: \n', confusion_matrix(y_test, predictions))


## Deciding K!

error = []
print(error)

for i in range(1,15):
    knn = neighbors.KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)
    temp_pred = knn.predict(X_test)
    error.append(npy.mean(temp_pred != y_test))

plt.figure()
plt.plot(range(1,15), error, linestyle = 'dashed', marker = 's', markersize = 10)
plt.xlabel('K')
plt.ylabel('Error')
plt.title('Error vs. K')
plt.show()