#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 21:56:13 2018

@author: Journey
"""
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
    monthlyPayment = monthlyPaymentRate * balance
    balance = balance - monthlyPayment
    balance = balance + (monthlyInterestRate * balance)
    print("Month " + str(month) + " remaining balance: " + str(round(balance, 2)))

print("Remaining balance: " + str(round(balance, 2)))