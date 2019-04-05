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
    
    x = df.loc[:, df.columns != 'ASPFWR5']
    y = df['ASPFWR5']
    
    counter=1
    for train_index, test_index in tscv.split(x):
       x_train, x_test = x.iloc[train_index], x.iloc[test_index]
       y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
       model.fit(x_train, y_train)
       preds = model.predict(x_test)
       
       print(counter,": ", r2_score(y_test, preds))
       counter+=1
       

df = load()


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
"""
These plots indicate that the ASPFWR5 likely follows an AR(1) model, so we
only need to look at values from one time step beforehand
"""


#Correlations
#sns.heatmap(df.corr(), center=0, cmap='coolwarm')
#asp = df.corr()['ASP'].sort_values(ascending=False)
#ax = sns.barplot(y = asp.index, x=asp)

#Feature Importances
ax = sns.barplot(x=df.columns[df.columns != "ASPFWR5"][rf.feature_importances_ > 0.01], y=rf.feature_importances_[rf.feature_importances_ > 0.01])
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)





# NOTES
'''
Current Model: SAR(1, ?) x (?,?)
-need to difference out to acheive stationarity
    -use hyp test to check before and after differencing bc too much data for accurate visual check
-need to account for seasonality somehow
-VAR models suddenly looking a lot more promising
-can i test for seasonality somehow?
    -periodogram



this data feels dirty
first half of ASP is 0? doesnt sound right
    -do other metrics follow this pattern?

- Cant produce any meaningful models until differenced and const var!
    -how to difference when more vars than just Y? difference those too or leave them be? *****
    -multivariate time series analysis
    -when looking at performace metrics, do i look at the differenced or undifferenced data?
    
-BIC recommends lower order models than AIC?
    -figure out how the hell these actually work
    -also wtf is granger causality
        -two vars are granger causal if they have some correlation through time

honestly a fucking LSTM would be easier at this point
    -this might actually be a good idea
    -would still need to figure out how to difference    
    
VAR models are good apparantly
    
0. look at the covariance matrix! these R2 values are too good
1. find which variables depend on time (should be all but ive been surprised before)
2. difference those vars until stationary? 
    -do we only care about stationarity for the response variable?
    -why do i do this to myself?

'''