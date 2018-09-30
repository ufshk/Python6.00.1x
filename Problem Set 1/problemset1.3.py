# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'zyxwvutsrqponmlkjihgfedcba'
substr = ''
substr2 = ''

for i in range(len(s)):
    if s[i] >= s[i - 1]:
        substr += s[i]
    elif s[i] < s[i - 1]:
        if len(substr) > len(substr2):
            substr2 = substr
            substr = s[i]
        else:
            substr2 = substr2
            substr = s[i]

if len(substr2) >= len(substr):
    print("Longest substring in alphabetical order is: " + str(substr2))
else: 
    print("Longest substring in alphabetical order is: " + str(substr))