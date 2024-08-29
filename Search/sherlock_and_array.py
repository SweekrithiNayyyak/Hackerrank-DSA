#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    total_sum=sum(arr)
    left_sum=0
    for val in arr:
        right_sum=total_sum-left_sum-val

        if right_sum==left_sum:
            return "YES"
        left_sum+=val
    return "NO"
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
