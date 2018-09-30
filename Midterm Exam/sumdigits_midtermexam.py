#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:35:38 2018

@author: Journey
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        return N
    else:
        return sumDigits(N % 10) + sumDigits(N // 10)
    
        