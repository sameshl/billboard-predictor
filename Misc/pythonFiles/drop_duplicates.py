#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:23:24 2019

@author: wisecracker
"""
import pandas as pd
dataset = pd.read_csv("baa (copy).csv")
dataset1 = dataset.drop_duplicates(subset =dataset.columns[0:2], keep='last')
dataset1 = dataset1.reset_index(drop = True)
X = dataset1.iloc[:, 0]
print (X[0])
df = pd.read_csv("SongCSV1.csv")
df['SongID'].str.decode("utf-8")
print(df.columns)