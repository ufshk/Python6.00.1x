#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:30:52 2018

@author: Journey
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invertedDict = {}
    originalKeys = []
    originalValues = []
    
    for keyItem in d.keys():
        originalKeys.append(keyItem)
    
    for valueItem in d.values():
        originalValues.append(valueItem)
    
    for item in range(len(originalKeys)):
        if originalValues[item] in invertedDict.keys():
            invertedDict[originalValues[item]] += [originalKeys[item]]
        else:
            invertedDict[originalValues[item]] = [originalKeys[item]]
            
    for i in invertedDict:
        invertedDict[i].sort()
    
    return invertedDict