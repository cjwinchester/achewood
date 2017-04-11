from os import environ
import random
from flask import Flask, jsonify
from strips import strips as strip_ls

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def post():
    url_stub = 'http://achewood.com/comic.php?date='
    random_day = random.randint(0, len(strip_ls))
    strip = strip_ls[random_day]
    response = {
        "response_type": "in_channel",
        "text": url_stub + strip
    }
    return jsonify(response)


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
