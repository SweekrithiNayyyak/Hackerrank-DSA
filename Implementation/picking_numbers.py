#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    count = {}
    
    # Count the occurrences of each number
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    max_count = 0
    
    for num in count:
        # Calculate the count of the current number and the next number
        current_count = count[num] + count.get(num + 1, 0)
        max_count = max(max_count, current_count)
    
    return max_count
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
