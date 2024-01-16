# importing the modules
import requests
from bs4 import BeautifulSoup

# providing url
url = "https://auth.geeksforgeeks.org/user/adityaprasad1308/articles"

# creating requests object
html = requests.get(url).content

# creating soup object
data = BeautifulSoup(html, 'html.parser')

# finding parent <ul> tag
parent = data.find("body").find("ul")

# finding all <li> tags
text = list(parent.descendants)

# printing the content in <li> tag
print(text)
for i in range(2, len(text), 2):
	print(text[i], end=" ")
