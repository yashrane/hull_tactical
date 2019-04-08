# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019
    
@authors: shaiyon, yashr
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def load(filepath='dataset.csv', preprocess=True):
    # Load data from csv
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    
    # Drop rows
    df.dropna(axis=0, inplace=True)

    # Preprocess data for modeling 
    if preprocess:          
                                 
        # Separate features and targets
        X = df.drop('ASPFWR5', axis=1)
        y = df['ASPFWR5']
        
        # Standardize data
        X = StandardScaler().fit_transform(X)
            
        # Dimensionality reduction with principal component analysis 
        X = pd.DataFrame(PCA(n_components = 30).fit_transform(X))
        
        # Set index to datetime
        X.reindex(y.index)        
        df = pd.DataFrame(X.values, index=y.index)
        # Merge X and y
        df['ASPFWR5'] = y 
 
    return df

filepath = "C:\\Users\\shaiyon\\Documents\\Datasets\\S&P 500 Prediction\\dataset.csv"
df = load(filepath, preprocess=True)