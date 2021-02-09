# Import the necessary libraries
import pandas as pd
import numpy as np 

def df_info(df):
    '''
    @leosanchezsoler
    The function provides all the relevant info of a pandas.DataFrame
        Arguments:
            - df: a pandas.Dataframe
        Prints:
            - df.shape[0]: number of rows
            - df.shape[1]: number of columns
            - df.columns: the name of the dataset columns'
            - df.info(): basic info about the dataset
            - df.isna().sum(): NaN values per column
    '''
    print('####\nDATAFRAME INFO\n####')
    print('\nNumber of rows:', df.shape[0])
    print('Number of columns:', df.shape[1])
    print('\n#### DATAFRAME COLUMNS ####\n', df.columns, '\n')
    print('### DATAFRAME COLUMN TYPES ###\n')
    print('\n', df.info()) 
    print('\n### TOTAL NaN VALUES ###\n', '\n', df.isna().sum())