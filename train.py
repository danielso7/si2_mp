# 
# File: train.py
# Author: Daniel Oliveira
# Mec. Number: 89208
# Course: Sistemas Inteligentes II
# Date: 24th May of 2022
#

## Building a neural network to train our chatbot ##

# Initial dependencies #
import json
import pickle
from model import *
from utils import *

# Import Intents Dictionary #
                           
with open('intents.json', 'r') as jsondata:
    intents = json.load(jsondata)

# Stem Intents #
words, classes, patterns = prepareintents(intents)
pickle.dump(words, open('words.plk','wb'))
pickle.dump(classes, open('classes.plk','wb'))

# Prepare Data for Neural Network #
inputrain, outputrain = preparenn(words,classes,patterns)

# Train Neural Network #
model = NeuralNetwork(inputrain,outputrain)

