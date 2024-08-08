#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#
def bonAppetit(bill, k, b):
    total = sum(bill) - bill[k]
    per_person = total / 2
    return "Born Appetit" if b - per_person == 0 else int(b - per_person)
    # Write your code here


if __name__ == "__main__":
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # bill = list(map(int, input().rstrip().split()))

    # b = int(input().strip())
    n, k, bill, b = 4, 1, [3, 10, 2, 9], 12

    result = bonAppetit(bill, k, b)
    print(result)
