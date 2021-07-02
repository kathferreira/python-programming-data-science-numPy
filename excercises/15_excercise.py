# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:09:07 2021

@author: kferreip

Excercise 15

Using numpy create a two-dimensional array with the shape (10,4) pseudo-randomly generated values from the standard normal distribution N(0,1), Set the random seed to 20.

Tip: Use the function np.random.randn()


"""
import numpy as np

seed_array = np.random.seed(20)
seed_array = np.random.randn(10,4)

print(seed_array)

#Also
np.random.seed(20)
print(np.random.randn(10, 4))