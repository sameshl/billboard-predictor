#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:15:19 2019

@author: samesh
"""

import glob
import pandas as pd

df = pd.concat([pd.read_csv(f,sep="	",header=None) for f in glob.glob('*.txt')], ignore_index = True)