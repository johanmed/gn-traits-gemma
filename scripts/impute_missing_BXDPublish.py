#!/usr/bin/env python

import pandas as pd
import numpy as np

trimmed_BXD_data=pd.read_csv('../data/no_x_TrimmedBXDPublish.csv')

#print('Original trimmed data looks like: \n', trimmed_BXD_data.head())

trimmed_data=trimmed_BXD_data.iloc[:,1:]
lines=trimmed_BXD_data.iloc[:,0]

#print('New trimmed data looks like: \n', trimmed_data.head())

from sklearn.impute import KNNImputer

def impute_missing_values(dataset):
    """
    Use all features of dataset to impute iteratively missing values in columns with at least one non-missing values
    Return random imputed values drawn from Gaussian prediction of default estimator > 0.0
    """
    imputer=KNNImputer(missing_values=0.0) 
    new_dataset=imputer.fit_transform(dataset)
    features=imputer.get_feature_names_out()
    
    return new_dataset, features


imputed_BXD_data, traits=impute_missing_values(trimmed_data)
imputed_data=pd.DataFrame(imputed_BXD_data, columns=traits, index=list(lines))

#print('Imputed data is: \n', imputed_data.head())

imputed_data.to_csv("../data/ImputedBXDPublish.csv")

