#!/usr/bin/env python3

n, m, p = map(int, input().split())
ans = 0

while m <= n:
    m += p
    ans += 1

print(ans)