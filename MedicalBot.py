#conda activate py33
#conda deactivate
import random
import json
import pickle
import numpy as np
import speech_recognition as sr
from ChatbotWorking import get_response,clean_up_sentence,bag_of_words,predict_class,audio_text
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from P_scraping import scraper

lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
model=load_model('chatbotmodel.h5')


r=sr.Recognizer()
print("What's your emergency : ")
#print(sr.Microphone.list_microphone_names())
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio= r.listen(source)
        try:
            text = r.recognize_google(audio,language = 'en-IN')
            if(text=="finish"):
                break
            queries=audio_text(text)
            scraper(queries[0],queries[1])
        except:
            print("could you speak a little bit slower")