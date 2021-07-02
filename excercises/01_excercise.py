# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:17:31 2021

@author: kferreip

Excercise 1

Check if all elements from the following arrays return the logical value True:
    

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

Print result to the console as shown below

Tip: Use the function np.all()

Expected result:
    A: True
    B: False
    C: False
    D: True
"""
import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

for name, array in zip(list('ABCD'),[A,B,C,D]):
    print(f'{name}: {np.all(array)}')