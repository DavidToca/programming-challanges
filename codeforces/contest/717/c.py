import sys
import statistics
import math
import datetime
import collections

sys.setrecursionlimit(100000000)

from functools import lru_cache
from itertools import combinations
import heapq


mod = 1000000007

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))


def solve(*args, **kwargs):
    return 0



# cases = inp
# for case in range(1, cases):
# for case in range(cases):
#     solution = solve()
#     print("Case #{case}: ", solution)

# n = inp()
# s = strng()
# s = strl()
# arr = inp()
# print(jn(',',[1,2,3]))
# arr = list(map(int, input().split()))