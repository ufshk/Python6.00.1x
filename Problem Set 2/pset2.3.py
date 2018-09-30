#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:41:42 2018

@author: Journey
"""

balance = float(input("Enter balance: "))
annualInterestRate = float(input("Enter annual interest rate: "))

monthlyInterestRate = annualInterestRate / 12.0
balance_backup = balance
paymentLower = 0
paymentUpper = (balance * (1 + monthlyInterestRate) ** 12)/12.0
payment = (paymentUpper + paymentLower) / 2
epsilon = 0.01
loops = 0

while abs(balance) >= epsilon:
    balance = balance_backup
    for month in range(25 * 12):
        balance -= payment
        balance += (balance * monthlyInterestRate)
    if balance < 0:
        paymentUpper = payment
        payment = (paymentUpper + paymentLower) / 2
    elif balance > 0:
        paymentLower = payment
        payment = (paymentUpper + paymentLower) / 2
    loops += 1
        
print("Lowest Payment: ", round(payment, 2), "in", loops, "loops.")