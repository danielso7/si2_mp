# 
# File: chatbot.py
# Author: Daniel Oliveira
# Mec. Number: 89208
# Course: Sistemas Inteligentes II
# Date: 24th May of 2022
#

## Building a conversation agent ##

# Initial dependencies #
import pickle
import json
from utils import *
from tensorflow.keras.models import * 

# Import Intents Dictionary #                          
with open('intents.json', 'r') as jsondata:
    intents = json.load(jsondata)

# Import Preprocessed Words and Classes List #
words = pickle.load(open('words.plk','rb'))
classes = pickle.load(open('classes.plk','rb'))

# Import Trained Model #
model = load_model('chatmodel.h5')

# Run Conversational Agent #
while True:
    inputmsg = input("")
    prediction = predictclass(inputmsg, model, words, classes)
    result = findanswer(prediction,intents)
    print(result)
