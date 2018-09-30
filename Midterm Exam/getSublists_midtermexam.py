#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:21:25 2018

@author: Journey
"""

def getSublists(L, n):
    sublists = []
    for i in range(len(L)):
        sublists.append(list(L[i:i + n]))
    del(sublists[:len(sublists) - n:-1])
    return sublists