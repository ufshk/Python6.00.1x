#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:32:10 2018

@author: Journey
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
        
    if len(aStr) == 1:
        return aStr == char
    
    mid = len(aStr)//2
    mid_aStr = aStr[mid]
    if char == mid_aStr:
        return True
    elif char < mid_aStr:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid+1:])