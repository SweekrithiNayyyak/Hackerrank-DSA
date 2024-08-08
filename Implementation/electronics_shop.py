#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    l=[-1]
    for key in keyboards:
        for drive in drives:
            if key+drive<b:
                l.append(key+drive)

    return max(l)
        
    #
    # Write your code here.
    #

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # bnm = input().split()

    # b = int(bnm[0])

    # n = int(bnm[1])

    # m = int(bnm[2])

    # keyboards = list(map(int, input().rstrip().split()))

    # drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    keyboards,drives,b=[40,50,60],[5,8,12],60
    moneySpent = getMoneySpent(keyboards, drives, b)

    # fptr.write(str(moneySpent) + '\n')

    # fptr.close()
