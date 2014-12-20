import urllib2
import subprocess
from HTMLParser import HTMLParser

url = "http://apod.nasa.gov/apod/astropix.html"
response = urllib2.urlopen(url)
html = response.read()

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					if value[len(value)-3:len(value)] == "jpg":
						self.output = value

parser = MyHTMLParser()
parser.feed(html)
imgurl = parser.output

response = urllib2.urlopen("http://apod.nasa.gov/apod/" + imgurl)
img = response.read()

with open('img.jpg', 'w') as fh:
	fh.write(img)

pwd = subprocess.check_output('pwd')
command = 'gsettings set org.gnome.desktop.background picture-uri file://' + pwd.rstrip('\r\n') + '/img.jpg'
print command
subprocess.check_call(command, shell=True);
