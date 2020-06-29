#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
   steps=list(s)
   sealevel,vall,V=0,0,False
   for step in steps:
       if step =='D':
        
        if sealevel == 0:
            V=True
        sealevel-=1    
       else:
        sealevel+=1

        if sealevel==0 and V:
           vall+=1
           V=False
   return vall

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
