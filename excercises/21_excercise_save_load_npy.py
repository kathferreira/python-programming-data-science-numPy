# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:48:08 2021

@author: kferreip

Excercise 21

Using numpy create the array, save the array to a binary file named 'array.npy' and then load that file back into another variable. Print this variable to the console

Tip: Use the np.save() and np.load() functions

"""

import numpy as np

main_arr = np.arange(12)

print(main_arr)

print('----------')

reshaped_arr = main_arr.reshape(-1,4)

print(reshaped_arr)

print('----------')

np.save('array.npy',reshaped_arr)

loaded_file = np.load('array.npy')

print(loaded_file)

# Also
A = np.arange(12).reshape(-1, 4)
np.save('array.npy', A)
 
B = np.load('array.npy')
print(B)