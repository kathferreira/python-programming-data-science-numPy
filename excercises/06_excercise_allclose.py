# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:46:50 2021

@author: kferreip

Excercise 6

Check if the following arrays are equal (element-wise):

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

Use the np.allclose() function with default parameters and print result to the console

Expected result:
True

"""
import numpy as np


A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

print(np.allclose(A, B))