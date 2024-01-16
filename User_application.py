import random
import json
import pickle
import numpy as np
import speech_recognition as sr
from ChatbotWorking import get_response,clean_up_sentence,bag_of_words,predict_class,audio_text
import nltk
from nltk.stem import WordNetLemmatizer
import tkinter as tk
from tkinter import ttk
from flask import Flask, render_template, request,jsonify
from tensorflow.keras.models import load_model
from P_scraping import scraper
from MedicalBot import speech_recog
import warnings
warnings.filterwarnings("ignore")

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("initial.html")

@app.route('/bot')
def bot():
    text=speech_recog()
    result={}
    result['text']=text
    return jsonify(result)

if __name__ == '__main__':
   app.run(debug = True)
