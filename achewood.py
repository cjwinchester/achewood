from os import environ
import random
from flask import Flask, jsonify, request
from strips import strips as strip_ls

app = Flask(__name__)

token = environ.get('SLASH_TOKEN', None)


@app.route('/post', methods=['POST'])
def post():
    if request.form['token'] == token:
        url_stub = 'http://achewood.com/comic.php?date='
        random_day = random.randint(0, len(strip_ls))
        strip = strip_ls[random_day]
        response = {
            "response_type": "in_channel",
            "text": url_stub + strip
        }
    else:
        response = {
            "response_type": "whoops",
            "text": "oh man something went wrong"
        }
    return jsonify(response)


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
