'''
This script exemplifies Classification using Python tensorflow library with Keras API
For more details, see: https://www.tensorflow.org/api_docs/python/tf/keras/Model
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import metrics, datasets, preprocessing

import matplotlib.pyplot as plt
import pandas as pnd

# Lets use one of the built-in data set in scikit-learn library:
breast_cancer_data = datasets.load_breast_cancer() # Returns a dictionary

print(breast_cancer_data.keys())
print(breast_cancer_data.feature_names)

data = pnd.DataFrame(data = breast_cancer_data.data, columns = breast_cancer_data.feature_names)
data['target'] = breast_cancer_data['target']
print(data.head())

# The features are: 32 attributes, Classes are: M or B (Malignant or Benign)
# Details on data set is available here: https://scikit-learn.org/stable/datasets/index.html


# Splitting the data set into training and testing data. 33% of the data is kept as testing data:
X = data.drop('target', axis = 1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# Scaling Data:
scale = preprocessing.MinMaxScaler()
scale.fit(X_train)
X_train = scale.transform(X_train)
X_test = scale.transform(X_test)

# Creating the model and fitting it to the training data:

# This is a sequential neural network with 4 layers:
# Different types of activation functions are available: https://en.wikipedia.org/wiki/Activation_function
# we use here Rectified Linear Unit function.

model = Sequential()
model.add(Dense(15, activation = 'relu'))
model.add(Dense(15, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy')

model.fit(x = X_train, y = y_train, validation_data = (X_test, y_test), epochs = 200)

# Visualize the loss:
loss = pnd.DataFrame(model.history.history)
loss.plot()
plt.show()

# Testing the model:
print('Training Score: ', model.evaluate(X_train, y_train, verbose = 0))
print('Testing Score: ', model.evaluate(X_test, y_test, verbose = 0))

# Model evaluations:
predictions = model.predict_classes(X_test)
trainPredictions = model.predict_classes(X_train)
print('Training report: \n', metrics.classification_report(y_train, trainPredictions))
print('Testing report: \n', metrics.classification_report(y_test, predictions))
print('Confusion Matrix is: \n', metrics.confusion_matrix(y_test, predictions))