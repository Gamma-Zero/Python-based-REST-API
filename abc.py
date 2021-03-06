from flask import Flask, render_template, request, redirect, url_for, jsonify
from PIL import Image, ImageChops
from numpy import array
import urllib.request

app = Flask(__name__)

@app.route('/')
def abc():
    return render_template('abc.html')

@app.route('/image', methods=['POST'])
def upload_url():

    global url_req
    url_req=request.form['req']
    print(url_req)
    urllib.request.urlretrieve(url_req, "1.jpg")

    findcolor()

    return jsonify(
		logo_border=z,
		dominant_color=a
	)
    #return redirect(url_for('abc'))


def rgb2hex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)

def findcolor():
	
	img=Image.open("1.jpg")
	x,y=img.size
	l=img.getpixel((0,0))
	
	global z   # stores border color
	z=rgb2hex(l[0],l[1],l[2])
	
	d={}
	for i in range(x):
		for j in range(y):
			l=img.getpixel((i,j))
			w=rgb2hex(l[0],l[1],l[2])
			if(w in d):
				d[w]+=1
			else:
				d[w]=1
	
	global a   # stores dominant color
	a=0

	mx=-1
	for i in d:
		mx=max(mx,d[i])
	for i in d:
		if(mx==d[i]):
			a=i
			break

if __name__ == '__main__':
	#app.debug=True
	app.run()
