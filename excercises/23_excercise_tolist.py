# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:08:00 2021

@author: kferreip

Excercise 23

Create and convert the array into the list

Tip: use np.array.tolist() method

"""

import numpy as np

A = np.arange(12, dtype=int).reshape(-1,4)

print(A.tolist())
