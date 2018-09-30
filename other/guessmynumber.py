#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:02:08 2018

@author: Journey
"""
print("Please think of a number between 0 and 100!")
response = ''
guess = 50
high = 100
low = 0

while response != 'c':
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'h':
        high = guess
        guess = (high + low)//2
    elif response == 'l':
        low = guess
        guess = (high + low)//2
    elif response != 'h' and response != 'l' and response != 'c':
        print("Sorry, I did not understand your input")
        
print("Game over. Your secret number was: " + str(guess))