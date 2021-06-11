# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:26:37 2021

@author: 777
"""


number_of_terms = 4
start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start, end=" ")
    sum += start
    start = (start * 10) + 2
print("\nSum of above series is:", sum)

raqamlar = []
for n in range(1500,2701):
    if n%7==0 and  n%5==0:
        raqamlar.append(n)
print(raqamlar)