#!/usr/bin/env python3
from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))

m = defaultdict(list)
for i in range(n):
    m[a[i]].append(i+1)

for _ in range(q):
    x, k = map(int, input().split())
    if k <= len(m[x]):
        print(m[x][k-1])
    else:
        print(-1)