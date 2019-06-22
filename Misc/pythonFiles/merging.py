#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 01:28:44 2019

@author: samesh
"""
import re
import pandas as pd
songs=pd.read_csv('/home/samesh/PycharmProjects/ml_project/cleaned_hdf5.csv',error_bad_lines=False)
bill = pd.read_csv('/home/samesh/PycharmProjects/ml_project/cleaned_bill (copy).csv',error_bad_lines=False)

#bill.to_csv('cleaned_bill.csv',index=False)
#songs.drop(songs.columns[0],axis=1,inplace=True)
#print(songs.columns)
songs_new=songs.drop(['track_id','release','track_digitalid','artist_id', 'artist_digitalid','artist_hotness', 'artist_latitude', 'artist_location','artist_longitude', 'danceability', 'duration', 'energy', 'loudness','release_digitalid', 'song_hotness', 'song_id', 'tempo','time_signature', 'time_signature_confidence', 'year'],axis=1)
songs_new=songs_new.drop_duplicates()
trial_inner=pd.merge(songs_new,bill, left_on=['title','artist_name'],right_on=['title','artist_name'],how='inner')
def clean(col):
    return re.sub(r'\([^)]*\)', '', str(col))
    #return re.sub(r'\([^()]*\)', '', str(col))

songs['title']=songs['title'].apply(clean)

#trial_outer=pd.merge(songs,bill, on='Title',how='outer')
#trial_left=pd.merge(songs,bill, on='Title',how='left')
#trial_right=pd.merge(songs,bill, on='Title',how='right')
