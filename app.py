from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
import spotipy
import spotipy.util as util
from collections import namedtuple
from load import init
import pandas as pd
from sklearn.preprocessing import StandardScaler

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
global model, graph
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
        return redirect(url_for('predict', artist=artist, song=song))
    return render_template('index.html')


@app.route("/predict/<artist>/<song>")
def predict(artist, song):
    features = get_features(artist, song)
    # print(features)
    data = clean_features(features)
    # print(data[0])
    with graph.as_default():
        # perform the prediction
        # song_features = np.array(data.iloc[0])
        # print(song_features.shape)
        # print(song_features)
        pred = model.predict(data)
        # Multipling pred by 100 to get %
        pred = str(pred[0][0] * 100)
        # pred = pred * 100
        return pred

    # return render_template('predict.html', song=song, artist=artist, pred=pred)


def clean_features(features):
    data = pd.DataFrame([features])
    for i in range(0, 12):
        temp = {'danceability': 0.8, 'energy': 0.7, 'key': i,
                'loudness': -3, 'mode': 1,
                'speechiness': 0.08, 'acousticness': 0.6,
                'instrumentalness': 0,
                'liveness': 0.09, 'valence': 0.9, 'tempo': 96,
                'artist_score': 0}

        data = data.append(temp, ignore_index=True)
    # print(data)
    cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
            'artist_score']
    data = data[cols]
    mode = pd.get_dummies(data['mode'], drop_first=True)
    key = pd.get_dummies(data['key'], drop_first=True)
    data.drop(['mode', 'key'], axis=1, inplace=True)
    data = pd.concat([data, mode, key], axis=1)
    # Dropping all other temporary rows before using StandardScaler
    data.drop(data.index[1:], inplace=True)
    sc = StandardScaler()
    data = sc.fit_transform(data)
    return data


def get_features(artist, song):
    features = {}
    sp = authenticate()
    try:
        track_info = sp.search(q='artist:' + artist + ' track:' + song,
                               type='track')
        # print(track_info)
        track_id = track_info['tracks']
        track_id2 = track_id['items']
        if track_id2 != []:
            year = track_info['tracks']
            year_1 = year['items']
            year_2 = year_1[0]
            year_3 = year_2['album']
            year_4 = year_3['release_date']
            year_5 = year_4.split('-')
            if len(year_5) > 1:
                year_6 = year_5[0]
                track_id3 = track_id2[0]
                track_id4 = track_id3['id']
                month = year_5[1]
                feat_t = sp.audio_features(tracks=track_id4)
                feat = feat_t[0]

                danceability = feat['danceability']
                energy = feat['energy']
                key = feat['key']
                loudness = feat['loudness']
                mode = feat['mode']
                speechiness = feat['speechiness']
                acousticness = feat['acousticness']
                instrumentalness = feat['instrumentalness']
                liveness = feat['liveness']
                valence = feat['valence']
                tempo = feat['tempo']
        features = {'danceability': danceability, 'energy': energy, 'key': key,
                    'loudness': loudness, 'mode': mode,
                    'speechiness': speechiness, 'acousticness': acousticness,
                    'instrumentalness': instrumentalness,
                    'liveness': liveness, 'valence': valence, 'tempo': tempo,
                    'artist_score': 1}
        return features
    except Exception as e:
        print("Could not get data for", song, "by", artist, "Error:", e)


def authenticate():
    token = util.oauth2.SpotifyClientCredentials(
        client_id='578d6e7b02e3421c903fa7794aab9118',
        client_secret='b610ff6ee28b4b359098b97e384d7637')
    cache_token = token.get_access_token()
    spotify = spotipy.Spotify(cache_token)
    sp = spotipy.Spotify(auth=cache_token)
    print("Authenticated")
    return sp

    # @app.route("/about")
    # def about():
    #     return render_template('about.html', title='About')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    # predict('ed sheeran', 'shape of you')
