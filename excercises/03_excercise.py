# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:36:36 2021

@author: kferreip

Excercise 3

Check if any element of the following arrays return the logical value True:
    
A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

Print result to the console as shown below

Tipo: Use the np.any() function

Expected result:
    
    A: False
    B: True
    C: True
    D: True

"""

import numpy as np


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

for name, array in zip(list('ABCD'),[A,B,C,D]):
    print(f'{name}: {np.any(array)}')