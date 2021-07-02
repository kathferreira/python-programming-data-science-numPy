# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:40:37 2021

@author: kferreip

Excercise 4

Check if any element of the following arrays returns de logical value True along the axis with index 0

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

Print result to the console as shown below

Tip: Use the np.any() function with the axis argument

Expected result:
    A: [False False False]
    B: [False True False]
    C: [True False False]
    D: [True False]
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
    print(f'{name}: {np.any(array, axis=0)}')
