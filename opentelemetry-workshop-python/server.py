# TODO: add OTel init here

import logging
from flask import Flask, request
import sys

import requests

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(filename)s:%(funcName)s:%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.debug(
    "Log level is set to debug, spans will sent and printed to console"
)

@app.route("/")
def root():
    return "Click [Logs] to see spans!"


@app.route("/fib")
@app.route("/fibInternal")
def fibHandler():
    value = int(request.args.get('i'))
    if value == 1:
        returnValue = 0
    elif value == 2:
        returnValue = 1
    else:
        minusOnePayload = {'i': value - 1}
        minusTwoPayload = {'i': value - 2}

        respOne = requests.get(
            'http://127.0.0.1:5001/fibInternal', minusOnePayload)

        respTwo = requests.get(
            'http://127.0.0.1:5001/fibInternal', minusTwoPayload)

        returnValue = int(respOne.content) + int(respTwo.content)

    # this is a workaround for a glitch logging issue
    sys.stdout.write('\n')
    return str(returnValue)


if __name__ == "__main__":
    app.run(debug=True)
