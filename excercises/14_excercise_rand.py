# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:53:59 2021

@author: kferreip

Excercise 14

Set the random seed to 10. Then using numpy create a one-dimensional array consisting of 30 pseudo-randomly generated values from the uniform distribution [0,1] Print result to the console as show below

Tip: Use the function np.random.rand()

"""

import numpy as np
seed_array = np.random.seed(10)
seed_array = np.random.rand(30)

print(seed_array)

# Also
np.random.seed(10)
print(np.random.rand(30))
