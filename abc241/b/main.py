#!/usr/bin/env python3
from collections import defaultdict
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dict_A = defaultdict(int)

for i in range(n):
    dict_A[A[i]] += 1

ans = 'Yes'
for i in range(m):
    if dict_A[B[i]] == 0:
        ans = 'No'
    else:
        dict_A[B[i]] -= 1

print(ans)