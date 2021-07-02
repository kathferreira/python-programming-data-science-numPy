# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:48:43 2021

@author: kferreip

Excercise 19

Using numpy create a one-dimensional array (vector) containing the possible result from the Big Lotto Game. Set the random seed to 42

Tip: The result of this game is a 6-element vector of values from 1 to 49 inclusive.

Expected result

[14 46 48 45 18 28]

"""

import numpy as np

np.random.seed(42)
print(np.random.choice(range(1, 50), size=6, replace=False))