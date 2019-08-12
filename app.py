from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
from load import init
from Song import Song
from forms import SongForm, FeedbackForm

# TODO:
#
#       * add about page and write author info
#       * add feedback form page and give link to it on predict.html
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
app.config['SECRET_KEY'] = 'a51865b544b38a55894ce28f59f5b5fc'

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
    form = SongForm()
    if request.method == 'POST':
        artist = form.artist.data
        song = form.song.data
        choice = form.choice.data
        return redirect(url_for('predict', artist=artist, song=song,
                                choice=choice))

    return render_template('index_copy.html', form=form,
                           legend='Predict Song!',
                           title=' ')


@app.route("/about", methods=['GET'])
def about():
    form = FeedbackForm()
    if request.method == 'POST':
        name = form.name.data
        message = form.message.data
        email = form.email.data
    return render_template('about.html', form=form)


@app.route("/feedback")
def feedback_date():
    name = request.args.get('name')
    email = request.args.get('email')
    message = request.args.get('message')
    return about()


@app.route("/predict")
def predict():
    try:
        choice = request.args.get('choice')
        artist = request.args.get('artist')
        song = request.args.get('song')

        user_song = Song(artist=artist, song=song, choice=choice)

        # Get data in format for machine learning model
        data = user_song.data
        song_features = user_song.song_features
        (song_name, artist_name, song_url, popularity, preview_url,
         preview_img_urls) = user_song.extract_trackinfo()
        print(song_url)
        # print(data)
        # print(data[0])
        with graph.as_default():
            # perform the prediction
            pred = model.predict(data)
            pred = "{0:.3f}".format(pred[0][0] * 100)
            # Multipling pred by 100 to get %
            # pred = str(pred[0][0] * 100)
            # pred = pred * 100
            # print(pred)
            return render_template('predict_copy.html',
                                   song_name=song_name,
                                   artist_name=artist_name,
                                   song_url=song_url,
                                   preview_img_urls=preview_img_urls,
                                   popularity=popularity, preview_url=preview_url,
                                   pred=pred, song_features=song_features,
                                   title='Prediction')
    except Exception:
        return render_template('500.html')


if __name__ == '__main__':
    #   app.debug = True
    app.run(host='0.0.0.0', port=8000)
