import requests
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search
# link for extract html data

def getdata(url):
    r = requests.get(url)
    return r.text

h_tags=[]

query = "someone fainted"
URL=search(query)[1]  
print(URL)
#htmldata = getdata("https://www.geeksforgeeks.org/")
htmldata = getdata(URL)
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for data in soup.find_all("h2"):
    h_tags.append(data.get_text())


tag='h2'
for i in h_tags:
    if(i==" What to do when someone faints"):
        while(True):
            try:
                text2 = soup.find(tag, text=i).find_next('p').text
            except:
                break
            print(text2)
            tag='p'
            i=text2


#for data in soup.find_all("li"):
#    print(data.get_text())