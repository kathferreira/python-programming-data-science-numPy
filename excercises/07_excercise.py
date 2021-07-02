# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:50:01 2021

@author: kferreip

Excercise 7

Check if the following arrays are equal (element-wise)

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

Use the comparison operator == in this excercise and print the result to the console

Expected result:

    [False False True]

"""

import numpy as np


A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

# Solution I
print(A == B)

# Solution II
print(np.equal(A, B))