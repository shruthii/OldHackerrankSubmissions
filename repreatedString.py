#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the repeatedString function below.
def repeatedString(s, n):
    s=s.strip()
    sl=len(s)
    if s.count('a') == sl:
        return n
    result = (s.count('a') * (n//sl)) + s[:n%sl].count('a')
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
