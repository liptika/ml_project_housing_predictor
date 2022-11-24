from flask import Flask
import sys
app = Flask(__name__)
from housing.logger import logging
from housing.exception import HousingException

@app.route('/', methods=["GET", "POST"])
def index():
    try:
        raise("we are rasing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging")
    return 'logger done'


if __name__ == "__main__":
    app.run(debug=True)
