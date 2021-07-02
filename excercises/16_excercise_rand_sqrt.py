# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:13:43 2021

@author: kferreip

Excercise 16

Using numpy create a two-dimensional array with the shape (10,4) pseudo-randomly generated values from the normal distribution N(100,5). Set the random seed to 30

Tip: Use the function np.random.rand()


"""

import numpy as np
 
 
np.random.seed(30)
 
sigma = np.sqrt(5)
mu = 100
 
print(sigma * np.random.randn(10, 4) + mu)
