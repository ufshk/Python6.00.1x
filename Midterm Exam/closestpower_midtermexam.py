#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:12:56 2018

@author: Journey
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    difference_keeper = num
    power = 0
    for exponent in range(num):
        answer = base ** exponent
        difference = abs(answer - num)
        if difference < difference_keeper:
            difference_keeper = difference
            power = exponent

    return power