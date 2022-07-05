#A range of python packages
import pandas as pd
import numpy as np
import warnings
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')

# dropping some fields
def drop_df_cols(df_name, *args):
    """
    drops colums from a dataframe

    Parameters
    ----------
    df_name: dataframe name
        The name of a dataframe that the columns
        will be dropped from.
    
    *args: str
        a string  the name of a column in the 
        dataframe, seperate by commas.
        
    Example - (train_df, 'name', 'age')
    """ 
    to_drop = [item for item in args]
    print('----- Droped', to_drop)
    df_name.drop(to_drop, inplace=True, axis=1)

def visualise_missing_values(df_name, colours = ['#2F7B98','#2F7B98']):
    """
    Visualises missing values.

    Parameters
    ----------
    df_name: dataframe name
        The name of a dataframe to be
        visualised
    colours: the colours of the missing
    and non-missing values
    
    """
    cols = df_name.columns
    print('Blue is missing, Red is not missing')
    sns.heatmap(df_name[cols].isnull(), cmap=sns.color_palette(colours))
    print('number of NaN cols: ',df_name[cols].isnull().sum())
    df_name.dropna(axis='columns')
