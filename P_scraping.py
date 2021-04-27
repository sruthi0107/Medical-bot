import requests
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
# link for extract html data

def getdata(url):
    r = requests.get(url,verify=False)
    return r.text

def get_my_key(obj):
  return obj["similarity"]

h_tag_data=[]
h_tags=["h1","h2","h3","h4","h5","h6"]
query = "What to Do During a Heart Attack"
#print(search(query))
URL=search(query)[2]  
print(URL)
#htmldata = getdata("https://www.geeksforgeeks.org/")
htmldata = getdata("https://share.upmc.com/2015/07/what-to-do-if-someone-is-having-a-heart-attack/")
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
print(h_tag_data)
tag=h_tag_data[0]["tag"]
i=h_tag_data[0]["text"]
while(True):
    try:
        print("searching for p tags")
        text2 = soup.find(tag, text=i).find_next('p').text
        tag='p'
    except:
        try:
            print("searching for ul")
            #text2 = soup.find(tag, text=i).find_next('ul').text
            print("searching for li")
            #ul_tag=soup.find(tag, text=i).find_next('ul')
            text2 = list(soup.find(tag, text=i).find_next('ul').descendants)
        except:
            break
    print(text2)
    i=text2



#for data in soup.find_all("li"):
#    print(data.get_text())