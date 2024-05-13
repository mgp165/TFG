#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.ensemble import BaggingClassifier, BaggingRegressor
from lineartree import LinearTreeClassifier, LinearTreeRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, LogisticRegression
import numpy as np


# In[3]:


def LinearRandomForestClassifier(n_features, est=LinearTreeClassifier(base_estimator=LogisticRegression(), max_depth=3), n_est=5):
    
    '''
        A Classifier Random Forest made up of Linear Trees instead of  Decision Trees.
        
        Parameters
        ----------
        n_features : int
            The number of features in the train dataset.
            This is for selecting sqrt(n_features) for each estimator, like Random Forest does.
            
        est : object, default=LinearTreeClassifier(base_estimator=LogisticRegression(), max_depth=3)
            The base estimator to fit on random subsets of the dataset.
            The base estimator should be a Linear Tree with specified base_estimator and max_depth for itself.
        
        n_est : int, default=5
            The number of base estimators in the ensemble.
    '''

    lrf = BaggingClassifier(estimator=est, n_estimators=n_est, max_features=int(np.floor(np.sqrt(n_features))))
    
    return lrf


# In[5]:


def LinearRandomForestRegressor(n_features, est=LinearTreeRegressor(base_estimator=LinearRegression(), max_depth=3), n_est=5):
    
    '''
        A Regressor Random Forest made up of Linear Trees instead of  Decision Trees.
        
        Parameters
        ----------
        n_features : int
            The number of features in the train dataset.
            This is for selecting sqrt(n_features) for each estimator, like Random Forest does.
            
        est : object, default=LinearTreeRegressor(base_estimator=LinearRegression(), max_depth=3)
            The base estimator to fit on random subsets of the dataset.
            The base estimator should be a Linear Tree with specified base_estimator and max_depth for itself.
        
        n_est : int, default=5
            The number of base estimators in the ensemble.
    '''
    
    lrf = BaggingRegressor(estimator=est, n_estimators=n_est, max_features=int(np.floor(np.sqrt(n_features))))
    
    return lrf


# In[ ]:




