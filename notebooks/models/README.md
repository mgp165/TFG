## Models trained
For each dataset, several models have been trained, each on a different notebook. Their names correspond to:

- logistic_regression: [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) (and its variants with penalties) models for classification datasets.
  
- linear_regression: [Linear](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge), [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso) and [Elastic Net](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet) Regression models for regression datasets.
  
- decision_tree: [Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) or [Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor) Decision Trees models.

- random_forest: [Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) or [Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) Random Forest models.

- gradient_boosting: [Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html) or [Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor) Gradient Boosting models.

- xgboost: [Classifier](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBClassifier) or [Regressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor) XGBoost models.

- linear_tree: Linear Trees that are Decision Trees fitting Logistic/Linear Regression models at their nodes. Obtained from [this](https://github.com/cerlymarco/linear-tree) library.

- lrf: handmade Linear Random Forests ensambling [Bagging](https://scikit-learn.org/stable/modules/ensemble.html#bagging-meta-estimator) meta-estimators with Linear Trees as base estimators. Can be found [here](../utils/lrf.ipynb).

- rerf: Regression-Enhanced Random Forests based on [this](https://haozhestat.github.io/files/manuscript_HAOZHE_ZHANG.pdf) paper. Algorithms are from [this](https://github.com/cerlymarco/linear-tree) library. The classification ones have been modified, using Logistic Regression as base model instead of Linear Regression. 

- eblr: Explainable-Boosted Linear Regression based on [this](https://arxiv.org/pdf/2009.09110) work. Algorithms are from [this](https://github.com/cerlymarco/linear-tree) library.
  
## Notebooks structure
The steps that are carried out in every notebook from this folder are the following:

1. Upload the corresponding train, validation and test data.

2. Several models are fitted with the training data varying some hyperparameters and they are evaluated with the validation data.
   
3. The hyperparameters of the best model in terms of AUC/RMSE in the validation set are selected.
   
4. Train and validation sets are merged as retraining data.
   
5. A model with the optimal hyperparameters is trained with the retrain dataset and it is evaluated over the test set.
   
6. The trained model and the metrics obtained are saved.
