#(The google page found at the url is printed in ascii mode)
import urllib.request
url = "http://www.google.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
x = response.read()
f = open("google.html", "w")
f.write(str(x))