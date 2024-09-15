#!/usr/bin/env python3
from collections import defaultdict

q = int(input())
porch = defaultdict(int)
ans = 0

for _ in range(q):
    t, *x = map(int, input().split())
    if t == 1:
        porch[x[0]] += 1
        if porch[x[0]] == 1:
            ans += 1
    elif t == 2:
        porch[x[0]] -= 1
        if porch[x[0]] == 0:
            ans -= 1
    else:
        print(ans)
