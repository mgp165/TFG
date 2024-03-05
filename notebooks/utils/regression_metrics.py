#!/usr/bin/env python
# coding: utf-8

# We are creating a function for calculating the metrics of the models and saving them.

# In[1]:


import pandas as pd
import time
from sklearn.metrics import root_mean_squared_error


# In[2]:


def regression(list_models, list_names, path, X_train, y_train, X_test, y_test, metrics={}):
    
    for i in range(len(list_models)):
        model = list_models[i]
        name = list_names[i]
        start_time = time.time()
        model.fit(X_train, y_train)

        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)

        metrics[name] = {
            'Train_MSE': root_mean_squared_error(y_train, train_pred),
            'Validation_MSE': root_mean_squared_error(y_test, test_pred),
            'Run_Time': time.time() - start_time
        }
        
    metrics = pd.DataFrame.from_dict(metrics, orient='index',columns=['Run_Time', 'Train_RMSE', 'Validation_RMSE'])
    metrics['delta%'] = 100*(metrics.Validation_RMSE - metrics.Train_RMSE) / metrics.Train_RMSE
    
    metrics.to_csv(path)
    
    return metrics


# In[ ]:




