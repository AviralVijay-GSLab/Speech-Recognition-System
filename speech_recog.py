# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:22:17 2019

@author: GS-1854
"""

import speech_recognition as speech_recog

def speech_recognizer():
    # microphone starting
    record = speech_recog.Recognizer()
    with speech_recog.Microphone() as source:
        print("Say something!")
        audio = record.listen(source)

    # speech recognition using Google Speech Recognition
    try:
        output = record.recognize_google(audio)
        return output
    
    except record.UnknownValueError as e:
        return e
    
    except record.RequestError as e:
        return e

