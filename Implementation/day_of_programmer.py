#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def dayOfProgrammer(year):
    days_in_eight_month = 243

    if year == 1918:
        # Special case for the year of the calendar transition
        remaining_days = 256 - (days_in_eight_month - 13)
        return f"{remaining_days}.09.{year}"

    elif (
        (year < 1918 and year % 4 == 0)
        or (year % 4 == 0 and year % 100 != 0)
        or (year % 400 == 0)
    ):
        # Julian calendar or Gregorian leap year
        remaining_days = 256 - (days_in_eight_month + 1)
    else:
        # Non-leap year
        remaining_days = 256 - days_in_eight_month

    return f"{remaining_days}.09.{year}"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # year = int(input().strip())
    year = 1800

    result = dayOfProgrammer(year)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
