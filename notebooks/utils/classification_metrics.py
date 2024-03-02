#!/usr/bin/env python
# coding: utf-8

# We are creating a function for calculating the metrics of the models and saving them.


import pandas as pd
import time
from sklearn.metrics import roc_auc_score


def classification(list_models, list_names, path, X_train, y_train, X_test, y_test, metrics={}):
    
    for i in range(len(list_models)):
        model = list_models[i]
        name = list_names[i]
        start_time = time.time()
        model.fit(X_train, y_train)

        train_pred = model.predict_proba(X_train)[:, 1]
        test_pred = model.predict_proba(X_test)[:, 1]

        metrics[name] = {
            'Train_AUC': roc_auc_score(y_train, train_pred),
            'Validation_AUC': roc_auc_score(y_test, test_pred),
            'Run_Time': time.time() - start_time
        }
        
    metrics = pd.DataFrame.from_dict(metrics, orient='index',columns=['Run_Time', 'Train_AUC', 'Validation_AUC'])
    metrics['delta%'] = 100*(metrics.Validation_AUC - metrics.Train_AUC) / metrics.Train_AUC
    
    metrics.to_csv(path)
    
    return metrics
