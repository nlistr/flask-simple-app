import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/time')
def time():
    now = datetime.datetime.now()
    return str(now)

if __name__ == '__main__': 
    app.run(debug=True, port=8001)
