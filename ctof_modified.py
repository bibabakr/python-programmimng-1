#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:44:48 2017

@author: habiba

Python 

Write a program that converted Celsius degrees to Fahrenheit
Consider the following list:

temperatures=[10,-20,-289,100]

The lowest possible temperature that physical matter can reach is -273.15 °C. 
else print a warning message.


 
"""

temperatures=[10,-20,-289,100]

def ctof(c):
    if c >-273.15:
        f= c*9/5+32
        return f
    else:
        
     return "That temperature doesn't make sense!"

for t in temperatures :
    print(ctof(t))
    
    
    
