from os import environ
import random
import csv
from flask import Flask
from strips import strips as strip_ls

app = Flask(__name__)

webhook = environ.get('SLACK_WEBHOOK', None)


@app.route('/', methods=['GET'])
def index():
    return 'hello'


@app.route('/post', methods=['GET', 'POST'])
def post():
    url_stub = 'http://achewood.com/comic.php?date='
    random_day = random.randint(0, len(strip_ls))
    strip = strip_ls[random_day]
    return url_stub + strip


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
