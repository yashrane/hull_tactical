# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019

@author: yashr
"""
import pandas as pd
import numpy as np

def load(filepath='dataset.csv'):
    df = pd.read_csv(filepath)
    df = preprocess(df)
    return df
    


def preprocess(df):
    """Preprocess the given dataframe for later modeling"""
    
    #Create better date column
    df['date'] = pd.to_datetime(df['Unnamed: 0']).astype('int64')
    
    #Drop columns
    df.drop(['Unnamed: 0'], inplace=True, axis=1)
    
    #Transformations
    
    #their transformations arent actually improving our R2?
#    df['BDIY_MA'] = df['BDIY'].ewm(span=60).mean()
#    df['HS_MA_diff'] = df['HS'] - df['HS'].ewm(span=60).mean()
    
    
    #difference at lag 1
#    df.loc[:,df.columns != 'date'] = df.loc[:,df.columns != 'date'].diff()    
#    df_diff = df.loc[:,df.columns != 'date'].diff()    
  #    df = df.join(df_diff, how='outer', rsuffix='_d')
    df = df.join(df.shift(1), how='outer', rsuffix='_L1')    
     
    #Drop rows
    df.dropna(axis=0, inplace=True)
    
    return df




