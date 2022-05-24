import nltk
import random
import numpy as np
from nltk.stem import *
lem = WordNetLemmatizer()

def prepareintents(intents):
    words = []; classes = []; tokens = []
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            wordlist = nltk.word_tokenize(pattern)
            words.extend(wordlist)
            tokens.append((wordlist, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    words, classes = stemintents(words,classes)

    return words, classes, tokens

def stemintents(words,classes):
    charign = ['!','?','.',',']
    words = [lem.lemmatize(word) for word in words if word not in charign]
    words = sorted(set(words))
    classes = sorted(set(classes))

    return words, classes

def preparenn(words,classes,tokens):
    training = []
    output = [0]*len(classes)
    for token in tokens:
        queue = []
        pattern = token[0]
        pattern = [lem.lemmatize(word.lower()) for word in pattern]
        for word in words:
            queue.append(1) if word in pattern else queue.append(0)
        outputs = list(output)
        outputs[classes.index(token[1])] = 1
        training.append([queue, outputs])
    random.shuffle(training)
    training = np.array(training)
    xtrain = list(training[:,0])
    ytrain = list(training[:,1])

    return xtrain, ytrain

def predictclass(inputmsg, model, words, classes):
    sentence = preparesentence(inputmsg, words)
    result = model.predict(np.array([sentence]))[0]
    results = [[i,r] for i,r in enumerate(result) if r > 0.2]
    results.sort(key=lambda x: x[1], reverse=True)
    returnlist = []
    for r in results:
        returnlist.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return returnlist

def preparesentence(inputmsg, words):
    sentence = nltk.word_tokenize(inputmsg)
    sentence = [lem.lemmatize(word) for word in sentence]
    output = [0]*len(words)
    for w in sentence:
        for i, word in enumerate(words):
            if word == w:
                output[i] = 1

    return np.array(output)

def findanswer(prediction, intents):
    tag = prediction[0]['intent']
    intentlist = intents['intents']
    for i in intentlist:
        if i['tag'] == tag:
            result = random.choice(i['answers'])
            break

    return result