# si2_mp
# Sistemas Inteligentes II 2021/2022 - Mini-Projeto - Daniel Oliveira - 89208

# Building a conversational agent using Python, Flask and Javascript

This project was developed in Universidade de Aveiro, within the course of Sistemas Inteligentes II.

## 1st Deadline

1. Created an .json file with intents, that will help the chatbot to categorize the sentences. Only simple ones for now

2. Built a Neural Network for training the chatbot. It can be changed later as the number of intents grow.

3. Prepared data for the NN, using WordNet lemmatization and converting data in numerical values.

4. Using the NN model, the chatbot can now predict the class of one given sentence and choose one random answer from the available ones, of course inside that specific class.

## 2nd Deadline

1. Increased the number of intents, making the chatbot usable for a company.

2. Develop the ability to accumulate info from the client (current balance, state and name)

3. Develop the ability to answer user's requests (change password, buy/sell orders, change email)

3. Created a Flask app to run our chatbot in a website

4. Created a HTML/Javascript script to make the chatbot user-friendly

## Setup

1. Clone this repository and create a virtual environment

$ git clone 
$ cd si2_mp
$ python -m venv venv
$ . venv/bin/activate

2. Install dependencies and packages

$ (venv) pip install flask flask_mysqldb ntlk pickle random time requests
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')

## Run

1. Train the chatbot

$ (venv) python train.py

2. Run the app

$ (venv) python app.py

3. Go to website

http://localhost:5000/crexusers/

4. Login using one of the users 

Username: daniel
Password: pass1

5. Test the chatbot