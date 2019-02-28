#Ken Sherman
#HW 3

import requests
from requests import get
from requests import post
from bs4 import BeautifulSoup
import re
from nltk import sent_tokenize


male = list()
woman = list()
for i in range(50):
    while True:
        try:
#i had to use the while true statement because sometimes the website doesn't follow a sentence structure
            get_resp = get ("https://theyfightcrime.org/", timeout = 30)
            soup = (BeautifulSoup(get_resp.text, 'html.parser'))
            paragraphs = soup.find_all("p")[1].text
#print (paragraphs)

            x = (sent_tokenize(paragraphs))

            x2 = (''.join(x))

            a,b,c = x2.split('.')

    #print(a)
            male.append(a)
            woman.append(b)
        except ValueError:
            continue
        break

with open('male.txt', 'w') as m:
    m.writelines(male)

with open('woman.txt', 'w') as w:
    w.writelines(woman)

    















