#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
ans = defaultdict(int)

for i in range(len(A)):
    ans[A[i]] += 1

for i in range(n):
    if ans[i+1] != 4:
        print(i+1)
        break