'''
Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on
the New York Times homepage.

'''
import requests #makes http requests
from bs4 import BeautifulSoup #allows us to parse data


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')

#how to search for tags with classes
# headLines = soup.findAll('span',{"class":"ghost"})
headLines = soup.findAll('h2')
for headline in headLines:
    print(headline.get_text())
    print('\n')
