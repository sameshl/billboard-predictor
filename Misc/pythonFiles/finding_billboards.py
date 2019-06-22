#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 18:25:54 2019

@author: samesh
"""

import glob
import pandas as pd

bill = pd.read_csv('/home/samesh/PycharmProjects/ml_project/cleaned_bill (copy).csv',error_bad_lines=False)
#bill=bill.drop(['peakPos', 'lastPos', 'weeks', 'rank', 'isNew','billboardHit'],axis=1)

bill=bill.drop(['peakPos', 'lastPos', 'weeks', 'rank', 'isNew'],axis=1)

#songs = pd.concat([pd.read_csv(f,sep="	",header=None) for f in glob.glob('*.txt')], ignore_index = True)
#songs.to_csv('half_cleaned_hdf.csv',index=False)
#songs=pd.read_csv('/home/samesh/PycharmProjects/ml_project/half_cleaned_hdf.csv',error_bad_lines=False)
#songs=songs.drop(['track_id','release','track_digitalid','artist_id', 'artist_digitalid','artist_hotness', 'artist_latitude', 'artist_location','artist_longitude', 'danceability', 'duration', 'energy', 'loudness','release_digitalid', 'song_hotness', 'song_id', 'tempo','time_signature', 'time_signature_confidence', 'year'],axis=1)


#songs=songs.drop(songs.columns[0:2],axis=1)
#songs=songs.drop(songs.columns[1:3],axis=1)
#songs=songs.drop(songs.columns[2:],axis=1)
#songs.to_csv('more_cleaned_hdf5.csv',index=False)



songs=pd.read_csv('/home/samesh/PycharmProjects/ml_project/more_2_cleaned_hdf5.csv',error_bad_lines=False)
songs=songs.drop_duplicates()


trial_outer=pd.merge(songs,bill, left_on=['title','artist_name'],right_on=['title','artist_name'],how='outer')
#trial_inner=pd.merge(songs,bill, left_on=['title','artist_name'],right_on=['title','artist_name'],how='inner')

trial_outer=trial_outer[trial_outer['billboardHit']!=1]

trial_outer.drop(trial_outer.columns[2],axis=1,inplace=True)
trial_outer.to_csv('not_billboards_2.csv',index=False)

#trial_inner.to_csv('half_matched_billboards.csv',index=False)



