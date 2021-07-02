# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:31:43 2021

@author: kferreip

Excercise 17

Iterate trough the array and print each element to the console

Tip: Use the np.nditer() function

"""

import numpy as np

A = np.array([[1, 4, 3],
              [5, 2, 6]])

for x in np.nditer(A):
     print(x, end='\n')