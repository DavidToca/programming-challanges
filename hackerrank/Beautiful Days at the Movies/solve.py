#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(numb):
    return int(str(numb)[::-1])

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    response = 0
    for numb in range(i, j+1):
        reverse_numb = reverse(numb)
        if (abs(numb-reverse_numb)%k==0):
            response+=1
    return response

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

