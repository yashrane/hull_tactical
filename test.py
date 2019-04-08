# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:55:27 2019

Used for testing out different models and visualizations

@author: yashr
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import r2_score
import seaborn as sns

from statsmodels.tsa.stattools import acf, pacf
from load import load

sns.set(style='darkgrid')


def test(df, model):
    """Tests the R2 of given model using a time series cross validation"""
    
    tscv = TimeSeriesSplit(n_splits=5)
    
    x = df.loc[:, df.columns != 'ASPFWR5_T']
    y = df['ASPFWR5_T']
    
    counter=1
    for train_index, test_index in tscv.split(x):
       x_train, x_test = x.iloc[train_index], x.iloc[test_index]
       y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
       model.fit(x_train, y_train)
       preds = model.predict(x_test)
       
       print(counter,": ", r2_score(y_test, preds))
       counter+=1
       

df = load(pca_components=0)


# MODELING

rf = RandomForestRegressor(random_state=0, n_estimators=100)
test(df, rf)

#lr = LinearRegression()
#test(df,lr)





# VISUALIZATIONS

#Scatterplot
#sns.scatterplot(x="date", y='ASPFWR5', data=df, alpha=0.1)
#sns.scatterplot(x="date", y='ASPFWR5_d', data=df.tail(100))


#ACF and PACF plots
#sns.barplot(x=list(range(1,32)), y=acf(df['ASP'])[1:32])
#sns.barplot(x=list(range(1,32)), y=pacf(df['ASP'])[1:32])


#Correlations
#sns.heatmap(df.corr(), center=0, cmap='coolwarm')
#asp = df.corr()['ASP'].sort_values(ascending=False)
#ax = sns.barplot(y = asp.index, x=asp)

#Feature Importances
ax = sns.barplot(x=df.columns[df.columns != "ASPFWR5_T"][rf.feature_importances_ > 0.01], y=rf.feature_importances_[rf.feature_importances_ > 0.01])
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)





# NOTES
'''
-no apparant seasonality
-ASPFWR5 follows a rough AR(1) model

need to try:
    VAR model
    dimensionality reduction with PCA
    

RNN with minute level data?
 - look at Calvin's stock price predictor
'''