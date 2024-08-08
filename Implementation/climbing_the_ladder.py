#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Remove duplicates from ranked to get unique ranks
    ranked = sorted(set(ranked), reverse=True)
    ranks = []
    n = len(ranked)
    i = n - 1  # Start from the last index of ranked

    # For each player's score, determine the rank
    for score in player:
        # Move up the ranked list while player's score is greater than ranked score
        while i >= 0 and score >= ranked[i]:
            i -= 1
        # i + 1 gives the correct rank
        ranks.append(i + 2)
    return ranks
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
