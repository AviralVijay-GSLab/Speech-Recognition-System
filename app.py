# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:24:26 2019

@author: GS-1854
"""

from flask import Flask
from .speech_recog import speech_recognizer

app = Flask(__name__)

@app.route('/')
def speech_engine():
    print("Welcome")
    return "Welcome to Speech Authentication System"

@app.route('/speech_authenticate')
def speech_authentication(user_message):
    speech_re = speech_recognizer()
    if speech_re == user_message:
        return "Success"
    return "failure"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)