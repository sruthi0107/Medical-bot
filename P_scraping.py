import requests
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

# link for extract html data
def scraper(w_query,heading):
    def checkblock(url):
        r = requests.get(url)
        return r.status_code

    def getdata(url):
        r = requests.get(url)
        return r.text

    def get_my_key(obj):
        return obj["similarity"]

    h_tag_data=[]
    h_tags=["h1","h2","h3","h4","h5","h6"]
    query1=w_query
    query=heading
    URL=search(query1)  
    for i in range(len(URL)):
        if(checkblock(URL[i])!=200):
            continue
        htmldata = getdata(URL[i])
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        for Htag in h_tags:
            for data in soup.find_all(Htag):
                h_tag_data.append({"tag":Htag,"text":data.get_text()})

        for i in range(len(h_tag_data)):
            text=[h_tag_data[i]["text"],query]
            cv=CountVectorizer()
            count_matrix=cv.fit_transform(text)
            h_tag_data[i]["similarity"]=cosine_similarity(count_matrix)[0][1]

        h_tag_data.sort(key=get_my_key,reverse=True)
        if(h_tag_data[0]["similarity"]<0.6):
            continue
        tag=h_tag_data[0]["tag"]
        i=h_tag_data[0]["text"]
        j=1
        while(True):
            try:
                text2 = soup.find(tag, text=i).find_next('p').text
                tag='p'
            except:
                try:
                    text2=soup.find(h_tag_data[0]["tag"],text=h_tag_data[0]["text"]).find_next("p").find_next("ul").text
                    j=0
                except:
                    break
            print(text2)
            i=text2
            if(j==0):
                break
        if(j==0):
            break

scraper("what to do for sprain","Tips to aid healing")