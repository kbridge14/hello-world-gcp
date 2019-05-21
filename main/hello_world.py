#!/usr/bin/env python3

from flask import Flask
import sqlalchemy
import psycopg2
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Kerry!     "


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

