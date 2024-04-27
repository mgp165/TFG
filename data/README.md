# Data
This directory contains every file that is  related with the datasets.

## Raw 
This folder is where the downloaded datasets are. More info about the sources can be found in the README of this folder.

## Intermediate
In this folder there are notebooks where the data cleaning and data engineering are done.

## Model Input
There are 3 subfolders inside. Each one is intended for saving the training, validation and test subsets that will be given to the models for the training and evaluation.

## Model Output
There are 2 subfolders:
- Metrics
Here there is a csv file per dataset containing running times, training and validation AUC/RMSE and deltas.
- Models
Here are saved all the models with the best hyperparameters obtained in validation trained with train and validation together.
