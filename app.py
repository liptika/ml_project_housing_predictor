from flask import Flask
app = Flask(__name__)
from housing.logger import logging
@app.route('/', methods=["GET", "POST"])
def index():
    logging.info("We are testing logging")
    return 'looger done'


if __name__ == "__main__":
    app.run(debug=True)
