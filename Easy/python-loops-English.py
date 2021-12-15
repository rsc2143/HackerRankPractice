#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 06:23:53 2021

@author: rohit
"""
if __name__ == '__main__':
    n = int(input().strip())
    if(n >= 1 and n <= 20):
        for i in range(0,n):
            print(pow(i,2))