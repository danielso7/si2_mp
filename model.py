# 
# File: model.py
# Author: Daniel Oliveira
# Mec. Number: 89208
# Course: Sistemas Inteligentes II
# Date: 17th June of 2022
#

### Neural Network Build ###

## Import dependencies ##

from tensorflow.keras.models import * 
from tensorflow.keras.layers import * 
from tensorflow.keras.optimizers import *
import numpy as np

## Build Deep Neural Network to train our chatbot ##

def NeuralNetwork(input, output):
    
    model = Sequential()
    model.add(Dense(128,input_shape=(len(input[0]),),activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(output[0]),activation='softmax'))
    sgd = SGD(lr=0.01, decay=1e-6, momentum = 0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])

    history = model.fit(np.array(input), np.array(output), epochs=200, batch_size=5, verbose=1)
    model.save('chatmodel.h5', history)

    return model

## Save model to external file ##