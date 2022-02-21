# --------------------------------------------------------------------------------------
# Created By  : hey24sheep.com
# Created Date: 11th Feb 2022
# License : MIT
# version = 1.0
#
# Description : A small and quick template file for competitve programming
# --------------------------------------------------------------------------------------
import sys, io, os, math, bisect
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import permutations, combinations
from sys import stdin, stdout

# set max recurssion limit
sys.setrecursionlimit(100000000)
# 10**9+7 prime
mod = 1000000007
mod1 = 998244353
# helpers
ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1
def isprime(n):
    if (n == 1 or n == 0): return False
    for i in range(2, int(n**(1 / 2)) + 1):
        if (n % i == 0):
            return False
    return True
# fast input
input = stdin.readline
get_input = lambda: stdin.readline().strip()
get_int = lambda: int(get_input())
get_list = lambda: get_input().split()
get_int_list = lambda: list(map(int, get_list()))
get_float_list = lambda: list(map(float, get_list()))
# fast output
output_float = lambda val: (stdout.write(f"{val:.2f}\n") and stdout.flush())
output = lambda val: (stdout.write(str(val) + "\n") and stdout.flush())

# solve
testcases = get_int()

for t in range(1, testcases + 1):
    n = get_input()
    s = get_input()

    # print result
    # print(f'Case #{t}: {result}')
