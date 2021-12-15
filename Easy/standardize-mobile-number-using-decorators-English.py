#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:04:57 2021

@author: rohit
"""
import functools
def decorator_for_standardising(param_function):
    @functools.wraps(param_function)
    def wrapper(*args, **kwargs):
        ascending_order_of_numbers = param_function(*args, **kwargs)
        standardised_ascending_order_of_numbers = ['+91 ' + str(number)[0:5] + ' ' + str(number)[5:len(str(number))] for number in ascending_order_of_numbers]
        return standardised_ascending_order_of_numbers
    return wrapper 

@decorator_for_standardising    
def ascending_order_sort_function(param_list_of_numbers):
    list_standardised_order_of_numbers_as_str = []
    
    for number in param_list_of_numbers:
        if(len(str(number)) == 10):
            list_standardised_order_of_numbers_as_str.append(str(number))
        elif(len(str(number)) == 11 and str(number)[0] == '0'):
            list_standardised_order_of_numbers_as_str.append(str(number)[1:len(str(number))])
        elif(len(str(number)) == 12 and str(number)[0:2] == '91'):
            list_standardised_order_of_numbers_as_str.append(str(number)[2:len(str(number))])
        elif(len(str(number)) == 13 and str(number)[0:3] == '+91'):
            list_standardised_order_of_numbers_as_str.append(str(number)[3:len(str(number))])
        else:
            print(f"{number} is not a phone number")
    list_standardised_order_of_numbers_as_int = [int(number_str) for number_str in list_standardised_order_of_numbers_as_str]
    
    return sorted(list_standardised_order_of_numbers_as_int)

            
if __name__ == '__main__':
    input_list_of_numbers = []
    n = int(input("Enter the number of elements : "))
    for i in range(0,n):
        element = str(input())
        input_list_of_numbers.append(element)
    
    output_of_numbers = ascending_order_sort_function(input_list_of_numbers)
    for i in range(0,len(output_of_numbers)):
        print(output_of_numbers[i])

