#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:11:11 2019

@author: wisecracker
"""
import numpy as np
#import json
import csv
import traceback
import logging

import spotipy
#from spotipy import oauth2
import spotipy.util as util

token = util.oauth2.SpotifyClientCredentials(client_id='578d6e7b02e3421c903fa7794aab9118', client_secret='b610ff6ee28b4b359098b97e384d7637')
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)
sp = spotipy.Spotify(auth=cache_token)
print("Authenticated")
'''
file_object = open('/home/wisecracker/MAC_ML_PROJECT/Spotify/notbillboard2.csv', 'a')
csv_file_writer = csv.writer(file_object, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")
csv_file_writer.writerow(['Artist', 'Track', 'Year', 'Month', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness','Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo'])
'''
for i in range(0,1):
    artist = 'Cardi B'
    track = 'I Like It'
    #score = score_l[i]
    #label = label_l[i]
    try:
        track_info = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    except:
        print ("Track info not found" )
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################") 
        print ("###############################################################")
        print ("###############################################################")
        print ("###############################################################")        
        continue
    print(i,track_info)
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
            #artist_fl.append(artist_l[i])
            #track_fl.append(track_l[i])
            #year_fl.append(year_6)
            #month_fl.append(month)
            #score_fl.append(score_l[i])
            #label_fl.append(label_l[i])
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
            print(year_6)
            #csv_file_writer.writerow([artist, track, year_6, month, danceability, energy, key,loudness, mode, speechiness, acousticness, instrumentalness,liveness, valence, tempo])

