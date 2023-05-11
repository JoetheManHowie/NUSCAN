#!/usr/bin/env python3

########################################
### utility functions for dataframes ###
########################################
def df_col_eq_val(df, col, val):
    return df.loc[df[col]==val]

def df_col_to_numpy(df, col):
    return df[col].to_numpy()

######################################
### utility functions for plotting ###
######################################
def multi_plot():
    ...

