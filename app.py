from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def ssd_harness():
  return render_template('ssd_harness.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

