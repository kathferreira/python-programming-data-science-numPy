# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:43:49 2021

@author: kferreip

Excercise 5

Check if the following array has missing data (np.nan):
    
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

Print result to the console as shown below

Tip: Use the np.isnan() function

Expected result
[[False False False True]
 [False True False False]]
"""

import numpy as np


A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

print(np.isnan(A))