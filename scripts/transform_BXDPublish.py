#!/usr/bin/env python

from extract_relevant_BXD_traits_id import list_ids # get list of traits ids

import pandas as pd

bxd_publish=pd.read_csv('BXDPublish.csv') # read in BXD phenotype file
new_bxd_publish=bxd_publish.copy() # make a copy and work on it


def process_data(data):
    """
    Takes dataframe of BXD phenotypes called data
    Iterates through list of extracted traits ids and format items accordingly
    Searches for formatted traits id in columns of phenotype dataframe
    Saves phenotype found data in a new dataframe
    Return new dataframe called new_data
    """
    new_data=pd.DataFrame()
    new_data['id']=data.iloc[:, 0]
    for i in list_ids:
        j=i.strip()
        j=j.strip(', ')
        j= f'BXD_{j}'
        if j in data.columns:
            new_data[j]=data[j]
    return new_data

new_to_save=process_data(new_bxd_publish)
new_to_save.to_csv('TrimmedBXDPublish.csv', index=False) # save results in file
