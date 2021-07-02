# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:29:36 2021

@author: kferreip

Excercise 2
Check if all elements from the following arrays return the logical value True along the axis with index 1:
    
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

Print result to the console as shown below

Tip: Use the function np.all() with the axis argument.

Expected result:
    
    A: [True True]
    B: [True False]
    C: [False True]

"""

import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

for name, array in zip(list('ABC'),[A,B,C]):
    print(f'{name}: {np.all(array,1)}')
    
    
"""

for name, array in zip(list('ABC'),[A,B,C]):
    print(f'{name}: {np.all(array,axis=1)}')
    
"""