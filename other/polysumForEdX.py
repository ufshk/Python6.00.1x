#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:40:06 2018

@author: Journey
"""

from math import *
def polysum(n, s):
    """
    n: a positive number, float or int
    s: a positive number, float or int
    """
    area = (0.25 * n * s ** 2)/(tan(pi/n))
    periSquared = (n * s) ** 2
    
    polygonSum = area + periSquared
    return round(polygonSum, 4)