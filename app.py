from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

# from sqlalchemy import create_engine, asc, desc, \
#     func, distinct
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.serializer import loads, dumps

# from database_setup import Base, Things

# import random
# import string
# import logging
# import json
# import httplib2
# import requests


app = Flask(__name__)


# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# Display all things
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
