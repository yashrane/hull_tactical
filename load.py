# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019

@author: shaiyon
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 


def load(filepath='dataset.csv', standardize=True, pred_time=1):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    X, y = preprocess(df, standardize, pred_time)
    return X, y
    


def preprocess(df, standardize, pred_time):
    
    cols = df.columns
    
    # Set up target as ASPFWR5 in pred_time days in the future
    pred_name = "ASPFWR5_{}DAY".format(pred_time)
    df[pred_name] = df["ASPFWR5"].shift(pred_time, axis=0)
                 
    # Drop rows
    df.dropna(axis=0, inplace=True)
    
    # Separate features and targets 
    X = df.drop(pred_name, axis=1)
    y = df[pred_name]
    
    if standardize:
        # Standardize data
        X = pd.DataFrame((StandardScaler().fit_transform(X, y)), columns=cols)
    
    # Principal component analysis   
    #pca = PCA(n_components = 10)
    #pca.fit(df)
        
    return X, y


