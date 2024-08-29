#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    count_dict = {}

    # Increment count for elements in brr
    for num in brr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Decrement count for elements in arr
    for num in arr:
        count_dict[num] -= 1

    # The elements with non-zero count in the dictionary are missing in arr
    missing = [num for num, count in count_dict.items() if count > 0]

    # Since missing elements should be returned in sorted order
    missing.sort()

    return missing

    while len(arr) > 0:
        if arr[0] != brr[0]:
            l.append(brr.pop(0))

        else:
            arr.pop(0)
            brr.pop(0)
    while len(brr) > 0:
        l.append(brr.pop())
    l.sort()
    return l

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # m = int(input().strip())

    # brr = list(map(int, input().rstrip().split()))
    # arr = [11,4,11,7,13,4,12,11,10,14]
    # brr = [11,4,11,7,3,7,10,13,4,8,12,11,10,14,12]
    arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

    result = missingNumbers(arr, brr)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
