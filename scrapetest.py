from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

soup = BeautifulSoup(html, 'html.parser')

print(soup.findAll('<head>', 'magna'))
print(soup.find('sint'))