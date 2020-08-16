# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:05:03 2020

@author: Sonali Kabadi
"""

lis=[1,2,3,4,5]
tuple = (6,7,8,9,0)
dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four'}

c=int(input("1. Assigning elements to different lists\n2. Accessing elements from tuple\n3. Deleting dictionary elements\n\n"))
print("Enter your choice\n--------------------------------------------------------------------\n")
if c==1: 
    N=int(input("Enter no. of elements you want to assign to the list: "))
    for i in range(N):
        A=int(input())
        lis.append(A)
    print(lis)
        
elif c==2:
    n=int(input("enter the index of elememt of tuple to access: "))
    print(tuple[n])
    
else:
    N = int(input("ENter the key of dictionary element to delete"))
    del dict[N]
    print(dict)
    
   