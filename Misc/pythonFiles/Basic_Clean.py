#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:07:29 2019

@author: wisecracker
"""

import pandas as pd

dataset = pd.read_csv('/home/samesh/PycharmProjects/ml_project/Spotify_datasets/getting_more_data_not_billboards_1.csv',error_bad_lines=False)
#datase = dataset.drop(0, axis=0)
#datase.to_csv('/home/wisecracker/MAC_ML_PROJECT/spotify_not_billboards_2.csv')
#dataset1= datase.reset_index(drop = True)
X = dataset.iloc[:,2]
type(X[2121])
df=dataset[dataset["'Year'"]>2009]
df.to_csv('more_than_2009_1.csv',index=False)


#y = X[0]
#y = y.replace(y[0], "")
#X[0] = y

#print(X[0][0])
m=len(X.index)

for i in range(m):
    #y = X[i]
    #y = y.replace(y[0], "")
    X[i] = int(X[i])
    print(i,X[i])

df = X.to_frame()    
datase = pd.concat(df, axis=1)



y = dataset1.iloc[:, 5]