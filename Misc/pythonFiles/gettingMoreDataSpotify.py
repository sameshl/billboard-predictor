# mport matplotlib.pyplot as plt
import numpy as np
# import json
import csv
import traceback
import logging

import spotipy
# from spotipy import oauth2
import spotipy.util as util

token = util.oauth2.SpotifyClientCredentials(client_id='578d6e7b02e3421c903fa7794aab9118',
                                             client_secret='b610ff6ee28b4b359098b97e384d7637')
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)
sp = spotipy.Spotify(auth=cache_token)
print("Authenticated")

file_object = open('/home/samesh/PycharmProjects/ml_project/Spotify_datasets/getting_more_data_not_billboards_2.csv', 'a')
csv_file_writer = csv.writer(file_object, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")
csv_file_writer.writerow(
    ['Artist', 'Track', 'Year'])

artist_l = []
track_l = []
# score_l = []
# label_l = []
with open('/home/samesh/PycharmProjects/ml_project/final_raw_datasets/not_billboards_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            artist_l.append(row[1])
            track_l.append(row[0])
            # score_l.append(row[2])
            # label_l.append(row[3])
        line_count += 1

m = len(artist_l)
# artist_fl = []
# track_fl = []
# year_fl = []
# month_fl  = []
# score_fl = []
# label_fl = []

'''
danceability = np.zeros([m,1])
energy = np.zeros([m,1])
key = np.zeros([m,1])
loudness = np.zeros([m,1])
mode = np.zeros([m,1])
speechiness = np.zeros([m,1])
acousticness = np.zeros([m,1])
instrumentalness = np.zeros([m,1])
liveness = np.zeros([m,1])
valence = np.zeros([m,1])
tempo = np.zeros([m,1])
'''
j = 0
for i in range(308000, m):
    artist = artist_l[i]
    track = track_l[i]
    # score = score_l[i]
    # label = label_l[i]
    try:
        track_info = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    except:
        pass
    print(i, track_info)
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
            #track_id3 = track_id2[0]
            #track_id4 = track_id3['id']
            #month = year_5[1]
            #feat_t = sp.audio_features(tracks=track_id4)
            #feat = feat_t[0]
            # artist_fl.append(artist_l[i])
            # track_fl.append(track_l[i])
            # year_fl.append(year_6)
            # month_fl.append(month)
            # score_fl.append(score_l[i])
            # label_fl.append(label_l[i])
            '''
            danceability[j] = feat['danceability']
            energy[j] = feat['energy']
            key[j] = feat['key']
            loudness[j] = feat['loudness']
            mode[j] = feat['mode']
            speechiness[j] = feat['speechiness']
            acousticness[j] = feat['acousticness']
                instrumentalness[j] = feat['instrumentalness']
            liveness[j] = feat['liveness']
            valence[j] = feat['valence']
            tempo[j] = feat['tempo']
            j += 1
            '''
            #danceability = feat['danceability']
            #energy = feat['energy']
            #key = feat['key']
            #loudness = feat['loudness']
            #mode = feat['mode']
            #speechiness = feat['speechiness']
            #acousticness = feat['acousticness']
            #instrumentalness = feat['instrumentalness']
            #liveness = feat['liveness']
            #valence = feat['valence']
            #tempo = feat['tempo']

            csv_file_writer.writerow([artist, track, year_6])

'''
with open('spotify_notbillboards_1.csv', mode='a') as spotify_features:
    #sp_writer = csv.writer(spotify_features, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
    sp_writer = csv.writer(spotify_features, delimiter=',', lineterminator = '\n')
    sp_writer.writerow(['Artist','Track','Year','Month','Danceability','Energy','Key','Loudness','Mode','Speechiness','Acousticness','Instrumentalness','Liveness','Valence','Tempo'])
    for i in range(0,j-1):
        sp_writer.writerow([artist_fl[i],track_fl[i],year_fl[i],month_fl[i],danceability[i][0],energy[i][0],key[i][0],loudness[i][0],mode[i][0],speechiness[i][0],acousticness[i][0],instrumentalness[i][0],liveness[i][0],valence[i][0],tempo[i][0]])
'''