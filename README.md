# Real-Estate-Market-Prediction-Project
End-to-End Real Estate Market Price Prediction Project - Machine Learning Project

##### App link on AWS : [Real Estate Market Price Prediction Project](http://ec2-15-237-137-129.eu-west-3.compute.amazonaws.com/)

## Description:
#### Developing a Machine Learning App about Real Estate Price Prediction for a region in Asia with deployment on AWS EC2.
* Cleaning data with Python extracted from Kaggle Dataset about "Banglore Home Prices" containing nearly 13.3k records by handling missing values and normalize property size.
* Detecting anomalies and removing outliers by adding the feature of "price per square meter", besides converting categorical data using Pandas dummies technique.
* Building linear regression, Lasso and decision tree models using Scikit-learn then tuning the hyperparameters using GridSearchCV, as result choosing the Lasso model based on score accuracy.
* Creating a Python Flask server to provide model APIs then deploy the app to production on AWS EC2.


### Details:
1. The data used in the project are from kaggle.com covering the details of "Banglore home prices".
1. The data can be found in [/model/](https://github.com/sakuragi97/Real-Estate-Market-Prediction-Project/tree/master/model) or [Kaggle](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data)
1. The project was built using Jupyter Notebook on **PyCharm 2020.2.5** as IDE
1. **Python** version **3.7**

Libraries used in the project:

* Numpy and Pandas for data cleaning
* Matplotlib and Seaborn for data visualization
* Sklearn for model building

* Jupyter Notebook, Visual Studio Code and PyCharm as IDE
* Python Flask for Back-End
* HTML/CSS/Javascript for Front-End

## App deployed on AWS EC2

* NGINX as Webserver

Server deployment requirement:
```
- Flask==1.1.2
- numpy==1.19.4
- scikit-learn==0.23.2
```
