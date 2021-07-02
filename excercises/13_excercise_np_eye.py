# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:46:32 2021

@author: kferreip

Excercise 13

Using numpy create a 6x6 two dimensional array - identity matrix with int data type.

Tip: Use the np.eye() function

"""

import numpy as np

eye_array = np.eye(N=6,M=6,k=0,dtype=int)

print(eye_array)

# Also
print(np.eye(N=6, dtype='int'))
