# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:35:17 2021

@author: kferreip

Excercise 12

Create an array with shape (9,10)

Tip: Use the np.arange() function and the np.ndarray.reshape() method

"""

import numpy as np

# Solution I

print(np.arange(10,100).reshape(-1,10))

# Solution II

print(np.arange(10,100).reshape(9,10))

# Solution III

print(np.arange(10,100).reshape(9,-1))