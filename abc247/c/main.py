#!/usr/bin/env python3
n = int(input())

def func(k):
    if k == 1:
        return [1]
    else:
        return func(k-1) + [k] + func(k-1)
    

ans = func(n)
print(*ans)