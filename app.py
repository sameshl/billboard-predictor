from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash
import spotipy
import spotipy.util as util

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
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search = request.form
        artist = search['artist']
        song = search['song']
        return redirect(url_for('song', artist=artist, song=song))
    return render_template('index.html')


@app.route("/song/<artist>/<song>")
def song(artist, song):
    features = get_features(artist, song)
    print(features)
    return render_template('search_result.html', song=song, artist=artist)


def get_features(artist, song):
    features = ()
    sp = authenticate()
    try:
        track_info = sp.search(q='artist:' + artist + ' track:' + song, type='track')
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
        features = (danceability, energy, key, loudness, mode, speechiness,
                    acousticness, instrumentalness, liveness, valence, tempo)
        return features
    except:
        print("Could not get data for", song, "by", artist)


def authenticate():
    token = util.oauth2.SpotifyClientCredentials(
        client_id='578d6e7b02e3421c903fa7794aab9118', client_secret='b610ff6ee28b4b359098b97e384d7637')
    cache_token = token.get_access_token()
    spotify = spotipy.Spotify(cache_token)
    sp = spotipy.Spotify(auth=cache_token)
    print("Authenticated")
    return sp

    # @app.route("/about")
    # def about():
    #     return render_template('about.html', title='About')
if __name__ == '__main__':
    # app.debug = True
    # app.run(host='0.0.0.0', port=8000)
