'''
This script exemplifies Regression using Python tensorflow library with Keras API
For more details, see: https://www.tensorflow.org/api_docs/python/tf/keras/Model
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import metrics, datasets

import matplotlib.pyplot as plt
import pandas as pnd
import numpy as npy

# Lets use one of the built-in data set in scikit-learn library:
data = datasets.load_diabetes()
print(data.keys())

features = pnd.DataFrame(data['data'])
target = pnd.DataFrame(data['target'])

# Features: 10 baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained
# for each of n = 442 diabetes patients, as well as the response of interest.
# Target: quantitative measure of disease progression one year after baseline.

# Splitting the data set into training and testing data. 20% of the data is kept as testing data:
trainingFeatures, testingFeatures, trainingTarget, testingTarget = train_test_split(features, target, test_size = 0.3, random_state = 42)

# Creating the model and fitting it to the training data:

# This is a sequential neural network with 4 layers:
# Different types of activation functions are available: https://en.wikipedia.org/wiki/Activation_function
# we use here Rectified Linear Unit function.

model = Sequential()
model.add(Dense(4, activation = 'relu'))
model.add(Dense(4, activation = 'relu'))
model.add(Dense(4, activation = 'relu'))
model.add(Dense(1))

model.compile(optimizer = 'rmsprop', loss = 'mse')

model.fit(x = trainingFeatures, y = trainingTarget, validation_data = (testingFeatures.iloc[1:], testingTarget.iloc[1:]), epochs = 200)
# higher epochs is better

# Visualize the loss:
loss = pnd.DataFrame(model.history.history)
loss.plot()

# Testing the model:
predictions = model.predict(testingFeatures)

print('\nMean Absolute Error for Testing:', metrics.mean_absolute_error(testingTarget, predictions))
print('Mean Squared Error for Testing:', metrics.mean_squared_error(testingTarget, predictions))
print('Root Mean Squared Error for Testing:', npy.sqrt(metrics.mean_squared_error(testingTarget, predictions)))

plt.figure(2)
plt.scatter(testingTarget,predictions)
plt.show()

# Predict a data that is not used in training:
new_data = testingFeatures.iloc[0].values.reshape(-1,10)
print('\nThe predicted value of th new data is: ', model.predict(new_data))
print('The correct value of the new data is: ', testingTarget.iloc[0])