#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_max_array=[]
    for i in range(len(arr)):
        min_max_array.append(sum(arr)-arr[i])
    print(min(min_max_array),max(min_max_array))
    
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
