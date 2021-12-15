#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:13:08 2021

@author: rohit
"""

if __name__ == "__main__":
    n = int(input().strip())
    def python_if_else(param_n):
        try:
            if(n > 0):
                if(n % 2 != 0):
                    print("Weird")
                else:
                    if(n >= 2 and n <= 5):
                        print("Not Weird")
                    elif(n >= 6 and n <= 20):
                        print("Weird")
                    else:
                        print("Not Weird")
        except:
            pass
    python_if_else(param_n=n)
        