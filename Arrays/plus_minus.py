#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive,negative,zero=0,0,0
    for i in arr:
        if i>0:
            positive+=1
        elif i==0:
            zero+=1
        else:
            negative+=1
       
    print(f"{positive/len(arr):.6f}")
    print(f"{negative/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
