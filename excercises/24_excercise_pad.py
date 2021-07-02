# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:19:42 2021

@author: kferreip

Excercise 25

Transform the array and print

Tip: Use the np.pad() function

"""

import numpy as np

A = np.ones(shape=(4, 4))
print(np.pad(A, pad_width=1, constant_values=0))