from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
from load import init
from Song import Song

#     func, distinct
# from sqlalchemy import create_engine, asc, desc, \
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

# global vars for easy reusability
global model, graph, sc
# initialize these variables
model, graph = init()
# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# Display all things
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search = request.form
        artist = search['artist']
        song = search['song']
        # print("###################", search)
        choice = request.form['options']
        return redirect(url_for('predict', artist=artist, song=song,
                                choice=choice))
    return render_template('index.html')


@app.route("/predict")
def predict():
    choice = request.args.get('choice')
    artist = request.args.get('artist')
    song = request.args.get('song')

    user_song = Song(artist=artist, song=song, choice=choice)

    # Get data in format for machine learning model
    data = user_song.data
    # print(features)
    # print(data)
    # print(data[0])
    with graph.as_default():
        # perform the prediction
        # song_features = np.array(data.iloc[0])
        # print(data)
        # print(song_features)
        pred = model.predict(data)
        # Multipling pred by 100 to get %
        pred = str(pred[0][0] * 100)
        # pred = pred * 100
        print(pred)
        return pred

    return render_template('predict.html', song=song, artist=artist, pred=pred)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
