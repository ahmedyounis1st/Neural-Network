# -*- coding: utf-8 -*-
"""logistic_regression_keras_mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B44oaIwX3cmzeEDwUXJORGDi1RxmRNsx
"""

import numpy as np
from tensorflow import keras
print (keras.__version__)

from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train.shape

from collections import Counter
Counter(y_train)

X_train_final = X_train.reshape(-1,784)
X_train_final.shape

X_test_final = X_test.reshape(-1,784)
X_test_final.shape

X_train_final = X_train_final / 255
X_test_final = X_test_final / 255

model = keras.Sequential()

# First Hidden Layer
model.add(keras.layers.Dense(512, input_shape= (784,), activation = 'relu'))
# Output Layer
model.add(keras.layers.Dense(10, activation = 'softmax'))

model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

results = model.fit(
    x = X_train_final,
    y = y_train,
    shuffle = True,
    epochs = 30,
    batch_size = 16,
    validation_data = (X_test_final, y_test)
)

eval = model.evaluate(x = X_test_final, y = y_test)

import matplotlib.pyplot as plt

plt.plot(results.history['loss'])
plt.plot(results.history['val_loss'])
plt.legend(['Training', 'Validation'])
plt.title('Training and Validation Losses')
plt.xlabel('epoch')
plt.ylabel('Losses')

plt.plot(results.history['accuracy'])
plt.plot(results.history['val_accuracy'])
plt.legend(['Training', 'Validation'])
plt.title('Training and Validation accuarcy')
plt.xlabel('epoch')
plt.ylabel('accuarcy')

model.summary()