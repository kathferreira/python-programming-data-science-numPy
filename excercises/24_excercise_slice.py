# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:10:18 2021

@author: kferreip

Excercise 24

Transform the array using slice operator

"""

import numpy as np

A = np.arange(12, dtype='int').reshape(-1, 4)
print(A[::-1])