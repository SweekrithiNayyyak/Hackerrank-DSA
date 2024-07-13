#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
   
    primary=0
    secondary=0
    for i in range(len(arr)):
        primary+=arr[i][i]
        secondary+=arr[i][len(arr)-i-1]
    print(abs(primary-secondary)) 
    
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    arr = []
    arr=[[11,2,4],[4,5,6],[10,8,-12]]


    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
