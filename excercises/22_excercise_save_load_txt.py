# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:57:19 2021

@author: kferreip

Excercise 22

Create the array then save it to a text file named 'array.txt' with two decimal places and then load this file back into another variable. Print this variable to the console.

Tip: Use the np.savetxt() and np.loadtxt() functions

"""

import numpy as np

A= np.arange(12).reshape(-1,4)

np.savetxt('array.txt',A)
# Also - np.savetxt(fname='array.txt', X=A, fmt='%0.2f')

B = np.loadtxt('array.txt')

print(B)