#!/usr/bin/env python3
from collections import defaultdict
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)
ans = defaultdict(int)

for i in range(len(C)):
    ans[C[i]] = i+1

for i in range(n):
    print(ans[A[i]], end=' ')

print()
for i in range(m):
    print(ans[B[i]], end=' ')