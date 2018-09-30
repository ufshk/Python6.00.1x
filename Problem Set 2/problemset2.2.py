#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 22:15:27 2018

@author: Journey
"""

payment = 0
balance_backup = balance

while balance > 0:
    balance = balance_backup
    payment += 10
    for month in range(12):
        balance -= payment
        balance += ((annualInterestRate / 12.0) * balance)
    
print("Lowest Payment: " + str(payment))