#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count=0
count1=0
for i in range(n):
    #print(i)
    #print (count)
    for j in range(n-1):
        if a[j]> a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count1=count1+1
    #print (count1)
print("Array is sorted in {} swaps.".format(count1))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))
            
