import flask
import os
import requests
import urllib.parse
import sqlite3


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/calligraphy')
def calligraphy():
    return flask.render_template('calligraphy.html')

@app.route('/creations')
def creations():
    return flask.render_template('creations.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/ssd_harness')
def ssd_harness():
    return flask.render_template('ssd_harness.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
