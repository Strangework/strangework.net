import flask
import os
import requests
import urllib.parse
import sqlite3


app = flask.Flask(__name__)


@app.route('/')
def ssd_harness():
    return flask.render_template('ssd_harness.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
