#!/usr/bin/env python3
from functools import cache

@cache
def solve(n):
    if n == 1:
        return 0
    else:
        return solve(n//2) + solve((n+1)//2) + n

print(solve(int(input())))