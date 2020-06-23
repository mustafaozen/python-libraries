'''
This script exemplifies Linear Regression using Python scikit-learn library
For more details, see: https://scikit-learn.org/stable/
'''

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as npy

# Lets use one of the built-in data set in scikit-learn library:
features, target = datasets.load_diabetes(True)

# Features: 10 baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained
# for each of n = 442 diabetes patients, as well as the response of interest.
# Target: quantitative measure of disease progression one year after baseline.

# Splitting the data set into training and testing data. 20% of the data is kept as testing data:
trainingFeatures, testingFeatures, trainingTarget, testingTarget = train_test_split(features, target, test_size = 0.2)

# Creating the model and fitting it to the training data:
lr = linear_model.LinearRegression()
lr.fit(trainingFeatures, trainingTarget)

# Testing the model:
predictions = lr.predict(testingFeatures)
trainPredictions = lr.predict(trainingFeatures)

# Model evaluations:
print('Mean Absolute Error for Training:', metrics.mean_absolute_error(trainingTarget, trainPredictions))
print('Mean Squared Error for Training:', metrics.mean_squared_error(trainingTarget, trainPredictions))
print('Root Mean Squared Error for Training:', npy.sqrt(metrics.mean_squared_error(trainingTarget, trainPredictions)))

print('\nMean Absolute Error for Testing:', metrics.mean_absolute_error(testingTarget, predictions))
print('Mean Squared Error for Testing:', metrics.mean_squared_error(testingTarget, predictions))
print('Root Mean Squared Error for Testing:', npy.sqrt(metrics.mean_squared_error(testingTarget, predictions)))

# Visualize the results:
plt.scatter(testingTarget,predictions)
plt.show()