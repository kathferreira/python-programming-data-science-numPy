# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:24:38 2021

@author: kferreip

Excercise 10

Using numpy, create an array 10x10 filled with number 255 and set the data type to float. Print this array to the console as shown below.

Tip: Use the np.ones() or np.full() functions

"""

import numpy as np

num_255_array = np.full(shape=(10,10),fill_value=255,dtype=float)

print(num_255_array)

#Solution I:

import numpy as np
 
 
print(np.ones(shape=(10, 10), dtype='float') * 255)

#Solution II:

import numpy as np
 
 
print(np.full(shape=(10, 10), fill_value=255, dtype='float'))