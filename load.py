# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019
    
@authors: shaiyon, yashr
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def load(filepath='dataset.csv', process=True, output="df", pca_components=0):
    # Load data from csv
    df = pd.read_csv(filepath)

    
    
    # Preprocess data for modeling (default)
    if process: 
        df = preprocess(df)
        if pca_components > 0:
            df = pca_preprocess(df, pca_components)

    #Drop rows
    df.dropna(axis=0, inplace=True)
                                     
    # Return single dataframe (default)
    if output=="df":
        return df
    
    # Return X and y otherwise
    else:
        X = df.drop('ASPFWR5', axis=1)
        y = df['ASPFWR5']
        return X, y


def pca_preprocess(df, pca_components):
    """Preprocess the given dataframe using PCA"""
    
    # Drop rows
    df.dropna(axis=0, inplace=True)
    
    # Separate features and targets
    X = df.drop('ASPFWR5', axis=1)
    y = df['ASPFWR5']
    
    # Dimensionality reduction with principal component analysis 
    X = StandardScaler().fit_transform(X)
    X = PCA(n_components = pca_components).fit_transform(X)
    
    # Set index to datetime
    df = pd.DataFrame(X, index=y.index)
    # Merge X and y
    df['ASPFWR5'] = y
    

    
    return df
    
def preprocess(df):
    """Preprocess the given dataframe for later modeling"""
    
    #changing date column to integer
    df = df.rename(columns={'Unnamed: 0':'date'})
    df['date'] = pd.to_datetime(df['date']).astype('int64')

    #df = df.join(df.shift(1), how='outer', rsuffix='_L1')
    
    #The change in features from the previous day
    df_diff = df.diff()    
    df = df.join(df_diff, how='outer', rsuffix='_d')
    
    #Target variable is the next day's ASPFWR5
    df['ASPFWR5_T'] = df['ASPFWR5'].shift(-1)    
    
    return df
