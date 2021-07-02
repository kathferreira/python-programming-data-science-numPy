# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:06:19 2021

@author: kferreip

Excercise 9

Using numpy create a 4x4 array filled with zeros (set data type to int). In response print this array to the console

Tip: Use the np.zeros() function

Expected result

[[0 0 0 0 ]
 [0 0 0 0 ]
 [0 0 0 0 ]
 [0 0 0 0]]

"""

import numpy as np

zero_array = np.zeros(shape=(4,4),dtype=int)

print(zero_array)