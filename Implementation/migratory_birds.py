#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    d = dict()
    for num in arr:
        if num in d.keys():

            d[num] += 1
        else:
            d[num] = 1
    max_val = max(d.values())
    l = []
    for k, v in d.items():
        if v == max_val:
            l.append(k)
    return min(l)

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 4, 4, 4, 5, 3]

    result = migratoryBirds(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
