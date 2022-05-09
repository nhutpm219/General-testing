#!/bin/python3

#input: 2 5
#output: 3.5

import math
import os
import random
import re
import sys


def avg(*n):
    sumOfNumber = 0
    for t in n:
        sumOfNumber = sumOfNumber + t
    avge = sumOfNumber / len(n)
    return avge

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
