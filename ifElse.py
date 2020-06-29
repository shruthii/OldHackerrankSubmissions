#!/bin/python3

N = int(input())
print ("Weird") if N%2 != 0 else (print ("Not Weird") if N in range(2,6) else (print("Weird") if N in range(6,21) else print("Not Weird")))

