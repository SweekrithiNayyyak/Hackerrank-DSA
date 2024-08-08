#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    am_or_pm = s[8:]

    s = s[:8]

    hrs, mim, sec = s.split(":")

    if am_or_pm == "AM" and hrs == "12":
        hrs = "00"
    if am_or_pm == "PM" and hrs != "12":
        hrs = str(int(hrs) + 12)
    return hrs + ":" + mim + ":" + sec

    # Write your code here


if __name__ == "__main__":

    s = "12:01:00AM"

    result = timeConversion(s)

    print(result)
