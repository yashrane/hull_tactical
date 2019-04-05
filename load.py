# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019

@author: yashr, shaiyon
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 


def load(filepath='dataset.csv'):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    df = preprocess(df)
    return df
    


def preprocess(df):
    """Preprocess the given dataframe for later modeling"""
    
    cols = df.columns
    
    # Target
    df["ASPFWR5_1DAY"] = df["ASPFWR5"].shift(1, axis=0)
                 
    # Drop rows
    df.dropna(axis=0, inplace=True)
    
    # Separate features and targets 
    X = df.drop("ASPFWR5_1DAY", axis=1)
    y = df["ASPFWR5_1DAY"]
    
    # Standardize data
    df = pd.DataFrame((StandardScaler().fit_transform(X)), columns=cols)
    
    # Principal component analysis   
    #pca = PCA(n_components = 10)
    #pca.fit(df)
        
    return df

df = load("C:\\Users\\shaiyon\\Documents\\Datasets\\S&P 500 Prediction\\dataset.csv")
print(df)


