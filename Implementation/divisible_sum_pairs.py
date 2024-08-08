#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    count = 0
    for num in range(n - 1):
        for j in range(num + 1, n):
            if (ar[num] + ar[j]) % k == 0:
                count += 1

    return count

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # ar = list(map(int, input().rstrip().split()))
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
