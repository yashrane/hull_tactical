# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:18:38 2019
    
@author: shaiyon
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def load(filepath='dataset.csv', preprocess=True, pred_days=1):
    # Load data from csv
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    
    # Set up target as ASPFWR5 in pred_days days in the future
    target = "ASPFWR5_{}DAY".format(pred_days)
    df[target] = df["ASPFWR5"].shift(-pred_days, axis=0)
    
    # Preprocess data for modeling 
    if preprocess:          
                         
        # Drop rows
        df.dropna(axis=0, inplace=True)
        
        # Separate features and targets
        X = df.drop(target, axis=1)
        y = df[target]
        
        # Standardize data
        X = StandardScaler().fit_transform(X)
            
        # Dimensionality reduction with principal component analysis 
        X = PCA(n_components = 30).fit_transform(X)
            
        return X, y
    
    return df