#!/usr/bin/env python3
n, h, x = map(int, input().split())
P = list(map(int, input().split()))

ans = 1000
for p in P:
    if x <= h + p:
        ans = min(ans, p)

print(P.index(ans)+1)