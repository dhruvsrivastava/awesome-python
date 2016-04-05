from flask import Flask , render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Hello World </h1>'

@app.route('/d3')
def d3():
	data = [1 , 5 , 10 , 15 , 20]
	return render_template('d3.html' , data = map(json.dumps , data) )

if __name__ == '__main__':
	app.run(debug = True)
