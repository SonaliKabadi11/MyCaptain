# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:51:07 2020

@author: Sonali Kabadi
Program: Print all +ve numbers in a list
"""


size = int(input('Enter the number of digits u want to enter:'))

li =[]
for i in range (size):
    li.append(int(input())) 

for i in range (0,size):
    if li[i]>=0:
        print(li[i] , end='\t')
        
        



