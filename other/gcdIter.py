#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:42:55 2018

@author: Journey
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    c = min(a,b)

    while c > 0:
        if(a%c) == 0 and (b%c) == 0:
            return c
        else:
            c -= 1
            print(c)