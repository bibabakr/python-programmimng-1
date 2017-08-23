#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:59:00 2017

@author: habiba
script that converts Celsius to Fahrenheit and 
creates a text file and stores the converted values inside the text file

Write a program that converted Celsius degrees to Fahrenheit
Consider the following list:

temperatures=[10,-20,-289,100]

The lowest possible temperature that physical matter can reach is -273.15 °C. 
Please don't write any message in the text file when 
input is lower than -273.15.


"""


t=[10,-20,-289,100]

def writer (t):
    with open ("ctof file handling results .txt",'w') as file :
        for c in t :
             if c >-273.15:
                 f=c*9/5+32
                 file.write(str(f)+"\n")
                 
writer(t)
                
                 