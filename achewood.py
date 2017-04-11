import requests
from datetime import date
from os import environ
import random
import csv
from time import sleep
from flask import Flask

app = Flask(__name__)

webhook = environ.get('SLACK_WEBHOOK', None)

url_stub = 'http://achewood.com/comic.php?date='
strip = '10012001'


@app.route('/', methods=['GET'])
def index():
    return 'hello'


@app.route('/post', methods=['POST'])
def post():
    try:
        with open('achewood.txt', 'r') as strips:
            ls = [row[0] for row in csv.reader(strips)]
            random_day = random.randint(0, ls.length)
            strip = ls[random_day]
    except FileNotFoundError:
        pass

    return url_stub + strip


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
