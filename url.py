import urllib

link = "http://www.somesite.com/details.pl?urn=2344"
f = urllib.urlopen(link)
myfile = f.read()
print myfile