#!/usr/bin/env python3
from collections import Counter

n = int(input())
A = list(map(int, input().split()))
c = Counter(A)
ans = n * (n-1) // 2

for i in c.values():
    ans -= i * (i - 1) // 2

print(ans)