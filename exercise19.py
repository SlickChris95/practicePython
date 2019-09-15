'''
Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on
this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4
pages. Your task is to print out the text to the
screen so that you can read the full article without
having to click any buttons.
'''
import requests #makes http requests
from bs4 import BeautifulSoup #allows us to parse data
import pprint
url ="http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r_html = requests.get(url).text
soup = BeautifulSoup(r_html,'html.parser')

# ps= soup.findAll('p')
# for p in ps:
#     print(p.get_text())
table = soup.findAll('div',class_="grid-items-2")
for x in table:
    pprint.pprint(x.find('p').text)

# print(r_html)
