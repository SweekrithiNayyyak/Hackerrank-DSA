#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    for num in grades:
        if num >= 38:
            #to find next multiple((num+(devisor-1)//divisor)*divisor)
            next_multiple_of_5 = ((num + 4) // 5) * 5
            if next_multiple_of_5 - num < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(num)
        else:
            rounded_grades.append(num)
    return rounded_grades
    # Write your code here


if __name__ == "__main__":

    # grades_count = int(input().strip())

    grades = []

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)
    grades = [73, 67, 38, 33]
    result = gradingStudents(grades)
    print(result)
