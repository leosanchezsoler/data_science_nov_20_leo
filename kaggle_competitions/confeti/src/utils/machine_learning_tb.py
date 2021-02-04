#Import the necessary libraries

import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error

def check_train_test_shape(X, y, X_train, y_train, X_test, y_test):
    '''
    @leosanchezsoler
    This function is used to check both training and testing sets' shape
        Arguments:
            - X: the intercept
            - y: the coef
            - X_train: the intercept's training set
            - y_train: the coef's training set
            - X_test: the intercept's test set
            - y_test: the coef's test set
    '''
    print('#### AVAILABLE DATA ####\n')
    print('X:', X.shape)
    print('y:', y.shape)
    print('\n#### TRAIN SETS ####\n')
    print('X_train:', X_train.shape)
    print('y_train:', y_train.shape)
    print('\n#### TEST SETS ####\n')
    print('X_test:', X_test.shape)
    print('y_test:', y_test.shape)

def predict(model, array):
    '''
    @leosanchezsoler
    For linearRegression
    A function that gets a sklearn model to make predictions based on a number

        Arguments:
            - model: a model from the sklearn library
            - array: an array with the size of the Features
    '''
    to_predict = np.array([number]).reshape(1, -1)
    return model.predict(to_predict)

def show_sklearn_metrics(y_test, predictions):
    '''
    @leosanchezsoler
    Prints significant loss functions in order to see our model error
        Arguments:
            - y_test: the target test set
            - predictions: our prediction model
        Prints:
            - MAE (Mean Absolute Error): the average error
            - MSE (Mean Squared Error): 'punishes' larger errors. More useful in the real world
            - RMSE (Root Mean Squared Error): is interpretable in the 'y' units
    '''
    print('MAE:', mean_absolute_error(y_test, predictions))
    print('\nMSE:', mean_squared_error(y_test, predictions))
    print('\nRMSE:', np.sqrt(mean_squared_error(y_test, predictions)))