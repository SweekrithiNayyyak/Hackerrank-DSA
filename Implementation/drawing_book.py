#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    forward_count=p//2
    n=n+1 if n%2==0 else n
    backward_pages=(n-p)//2
    
    return min([forward_count,backward_pages])
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # p = int(input().strip())
    n,p=6,5

    result = pageCount(n, p)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
