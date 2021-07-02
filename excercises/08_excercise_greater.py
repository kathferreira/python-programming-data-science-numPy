# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:52:40 2021

@author: kferreip

Excercise 8

The following arrays are given:

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

Check which numbers (element-wise) from the A array are greater than numbers from the B array and print result to the console as shown below

Expected result:
    [True False False False]
"""
import numpy as np


A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

# Solution I
print(A > B)

# Solution II
print(np.greater(A, B))

    
