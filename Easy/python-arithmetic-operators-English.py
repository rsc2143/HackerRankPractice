#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 06:06:33 2021

@author: rohit
"""
if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    if(a >= 1 and a <= pow(10,10) ):
        if(b >= 1 and b <= pow(10,10)):
            print(a+b)
            print(a-b)
            print(a*b)
            
    