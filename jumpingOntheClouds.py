#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    jum=0
    while i < (len(c) - 1):
        

        if i+2<n and c[i + 2] == 1:
            jump = 1
        else:
            jump = 2
        i = i + jump
        jum+=1

    return jum          

             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
