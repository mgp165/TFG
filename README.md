# Advanced Machine Learning with hybrid algorithms

This repository is intended for the practical part of my bachelor thesis (TFG in Spanish). It contains 6 datasets as examples of use cases with which the models studied in the project have been tested. More details can be found in the README of each directory. There is also the working memory (in Spanish).

## Abstract

This research carries out a theoretical overview of different supervised Machine Learning algorithms including parametric methods, such as regression, and non-parametrics ones, among which are decision trees-based methods, which involve CARTs themselves and the bagging and boosting families, with the purpose of presenting the state-of-the-art algorithms that combine both worlds.

The first part focuses on the mathematical aspect of the algorithms. To begin with, it is explained how the optimal coefficients are calculated in linear and logistic regression techniques. Then, the CART's training process is analysed in depth, laying the foundations for the successive models. Afterwards, the ideas behind Random Forest are sketched and the optimization processes that drive the functioning of Gradient Boosting and XGBoost are detailed.

The second part of the work introduces hybrid algorithms. First of all: Linear Tree, that is a CART fitting regression models at its nodes. In second place, it is proposed Linear Random Forest: a Random Forest made up of Linear Trees. It is followed by Regression-Enhanced Random Forest, that is a Random Forest trained over the errors made by a linear or logistic regression, enriching its predictions. Then it comes Explainable Boosted Regression, which implements non-linear relationships based on estimation errors in regression models. Lastly, Piecewise Linear Gradient Boosting is explained, providing extrapolation capability as well as software optimizations to the powerful boosting approach.

The final section is intended to make a comparison between all of the algorithms discussed theoretically during the work to prove whether these new methods that join decision trees and their derived methods with regressions are actually effective. Models are evaluated in terms of accuracy and running time along six exemplary use cases. In addition, possible future work to be investigated is suggested.
