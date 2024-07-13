#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    sp=n-1
    st=1
    for i in range(n):
        for _ in range(sp):
            print(" ", end="")
        for _ in range(st):
            print("#",end="")
        print()
        sp-=1
        st+=1
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
