#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    arr = []
    for cher in s:
        if cher in ['(', '{', '[']: arr.append(cher)
        else:
            if (cher == '}') and (getLastElement(arr) == '{'): del arr[-1]
            elif (cher == ')') and (getLastElement(arr) == '('): del arr[-1]
            elif (cher == ']') and (getLastElement(arr) == '['): del arr[-1]
            else: return 'NO'
   
    if len(arr): return 'NO'
    else: return 'YES'

def getLastElement(arr):
    if len(arr): return arr[-1]
    else: return None            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
