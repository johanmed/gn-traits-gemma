#!/usr/bin/env python

import pandas as pd

import os

data=os.listdir('../output/')

selected= [os.path.join('../output', i) for i in data if 'new_relevant' in i]


def concat_dataframes(selected):
    big_container=pd.DataFrame
    for x in selected:
        container=pd.read_csv(x)
        container.head()
        container_to_save=container['chr', 'pos']
        pd.concat([big_container, container_to_save])
        
    return big_container
    
result=concat_dataframes(selected)
result.to_csv('ML_database.csv')
