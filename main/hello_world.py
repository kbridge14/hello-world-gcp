#!/usr/bin/env python3

from flask import Flask
import sqlalchemy
import psycopg2
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
<<<<<<< HEAD
<<<<<<< HEAD
    return "Hello, Kerry! u r cool"
=======
    return "Hello, Kerry! What is up."
>>>>>>> 214cca2f596b0688ff16ae0ef37198f237780be0
=======
    return "Hello, Kerry!"
>>>>>>> 53b7cd17c89b2bda8554ac4bf98f55821df74157


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

