from flask import Flask
from flask import render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',data = "Hello")

@app.route('/author/<name>')
def author(name):
    return render_template('author.html',name = name)

if __name__ =='__main__':
    app.run(debug = True,port=8000)