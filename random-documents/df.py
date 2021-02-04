import pandas as pd 

def get_df_info(df):
    '''
                        ---what it does---
    df: pandas.DataFrame
    this function recieves a DataFrame as an argument and displays full information about its contents
    '''
    print('Dataframe info:', df.info())
    print('')
    