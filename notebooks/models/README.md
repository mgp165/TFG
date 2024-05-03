# Notebooks structure

The steps that are carried out in every notebook from this folder are the following:

1. Upload the corresponding train, validation and test data.
  
2. Several models are fitted with the training data varying some hyperparameters and they are evaluated with the validation data.
 
3. The hyperparameters of the best model in terms of AUC/RMSE in the validation set are selected.
  
4. Train and validation sets are merged as retraining data.

5. A model with the optimal hyperparameters is trained with the retrain dataset and it is evaluated over the test set.

6. The trained model and the metrics obtained are saved.
