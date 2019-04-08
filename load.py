# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019
    
@authors: shaiyon, yashr
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def load(filepath='dataset.csv', process=True, output="df", pca_components=30):
    # Load data from csv
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    
    # Drop rows
    df.dropna(axis=0, inplace=True)

    # Preprocess data for modeling (default)
    if process:  
        df = preprocess(df, pca_components)
                                     
    # Return single dataframe (default)
    if output=="df":
        return df
    
    # Return X and y otherwise
    else:
        X = df.drop('ASPFWR5', axis=1)
        y = df['ASPFWR5']
        return X, y


def preprocess(df, pca_components):
    # Separate features and targets
    X = df.drop('ASPFWR5', axis=1)
    y = df['ASPFWR5']
    
    # Standardize features
    X = StandardScaler().fit_transform(X)
    
    # Dimensionality reduction with principal component analysis 
    X = PCA(n_components = pca_components).fit_transform(X)
    
    # Set index to datetime
    df = pd.DataFrame(X, index=y.index)
    # Merge X and y
    df['ASPFWR5'] = y
    
    return df
    
    
