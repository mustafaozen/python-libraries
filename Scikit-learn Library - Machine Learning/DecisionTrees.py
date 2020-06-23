'''
This script exemplifies Decision Trees that can be used for both classification and regression problems,
using Python scikit-learn library.
For more details, see: https://scikit-learn.org/stable/
'''

from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import pandas as pnd

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


# Splitting the data set into training and testing data. 50% of the data is kept as testing data:
X = data.drop('target', axis = 1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# Creating the model and fitting it to the training data:
# As a criterion to decide the root node, we can use Entropy or Gini.
# This selection can change the performance as shown below:
dt1 = tree.DecisionTreeClassifier(criterion='entropy')
dt1.fit(X_train, y_train)

dt2 = tree.DecisionTreeClassifier(criterion='gini')
dt2.fit(X_train, y_train)

# Testing the model:
predictions1 = dt1.predict(X_test)
trainPredictions1 = dt1.predict(X_train)

predictions2 = dt2.predict(X_test)
trainPredictions2 = dt2.predict(X_train)

# Model evaluations:
print('Results when Entropy is used as criterion to decide the root node: \n')
print('Training report: \n', classification_report(y_train, trainPredictions1))
print('Testing report: \n', classification_report(y_test, predictions1))
print('Confusion Matrix is: \n', confusion_matrix(y_test, predictions1))

print('\n\nResults when Gini is used as criterion to decide the root node: \n')
print('Training report: \n', classification_report(y_train, trainPredictions2))
print('Testing report: \n', classification_report(y_test, predictions2))
print('Confusion Matrix is: \n', confusion_matrix(y_test, predictions2))