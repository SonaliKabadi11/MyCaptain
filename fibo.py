# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:05:01 2020

@author: Sonali Kabadi
Program: Fibonaci series
"""
def fib( n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))


num= int(input("Enter the number: "))
result = fib(num)
print(result)

