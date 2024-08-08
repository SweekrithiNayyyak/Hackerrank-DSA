#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    max_record = 0
    min_record = 0
    max_score, min_score = scores[0], scores[0]
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_record += 1
        elif score < min_score:
            min_score = score
            min_record += 1
    print(max_record, min_record)

    # Write your code here


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # scores = list(map(int, input().rstrip().split()))
    scores = [3,4,21,36,10,28,35,5,24,42]
    result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
