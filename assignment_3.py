# Binary Search Algorithm

import pandas as pd
import numpy as pd
from datetime import datetime

start = datetime.now()

def BinarySort(A, n, x):
    start = 0
    end = n -1
    while   start <= end:
        mid = int(round(start + end) / 2)
        if A[mid] == x:
            return mid
        elif x < A[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1
A = [2, 5, 8, 9, 11, 29, 32]
x = 11

print(BinarySort(A, len(A), x))

