# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:59:37 2020

@author: Pranav
"""

from matplotlib import pyplot as plt
from keras.datasets import mnist
from keras import utils 
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras import optimizers

(trainX, trainY), (testX, testY) = mnist.load_data()
print("TrainX shape {} TrainY shape {}".format(trainX.shape, trainY.shape))
print("TestX shape {} TestY shape {}".format(testX.shape, testY.shape))

plt.imshow(trainX[20])

trainX = trainX.reshape(60000, 28, 28, 1)
testX = testX.reshape(10000, 28, 28, 1)

trainY = utils.to_categorical(trainY)
testY = utils.to_categorical(testY)

model = Sequential()
model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(64, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

#model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
s_grad_d = optimizers.SGD(lr=0.01, decay=1e-6)
model.compile(optimizer=s_grad_d, loss='categorical_crossentropy', metrics =['accuracy'])
model.fit(trainX, trainY, validation_data=(testX, testY), epochs=3)