import urllib2
response = urllib2.urlopen('http://dooris.koalo.de/door.txt')
html = response.read()
print html
