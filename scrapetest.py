from urlib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())