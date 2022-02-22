#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    cnt = 0
        
    while(len(a) or len(b)):
        if len(a) and len(b):
            if a[0] < b[0]: least = a.pop(0)
            else: least = b.pop(0)
        elif len(a): least = a.pop(0)
        else: least = b.pop(0)      
        
        if maxSum>=0:
            maxSum -= least
            cnt += 1
        else: break
       
    return cnt

if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    fptr2 = open('input.txt', 'r')

    g = fptr2.readline()
        
    for _ in range(int(g)):
        first_multiple_input = fptr2.readline().strip().split(" ")

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, fptr2.readline().strip().split(" ")))

        b = list(map(int, fptr2.readline().strip().split(" ")))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
    fptr2.close() 
