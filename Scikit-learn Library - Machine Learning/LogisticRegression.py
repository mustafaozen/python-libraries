'''
This script exemplifies Logistic Regression using Python scikit-learn library
For more details, see: https://scikit-learn.org/stable/
'''

from sklearn import datasets, linear_model
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


# Splitting the data set into training and testing data. 30% of the data is kept as testing data:
X = data.drop('target', axis = 1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# Creating the model and fitting it to the training data:
logR = linear_model.LogisticRegression(max_iter = 200)
logR.fit(X_train, y_train)

# Testing the model:
predictions = logR.predict(X_test)
trainPredictions = logR.predict(X_train)

# Model evaluations:
print('Training report: \n', classification_report(y_train, trainPredictions))
print('Testing report: \n', classification_report(y_test, predictions))
print('Confusion Matrix is: \n', confusion_matrix(y_test, predictions))