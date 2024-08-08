#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    d=dict()
    for i in ar:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    total=0
    for v in d.values():
        total+=v//2
    return total
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    # n,ar=7,[1,2,1,2,1,3,2]

    result = sockMerchant(n, ar)
    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
