#!/usr/bin/env python3
n = int(input())
k = 1
x = 1

ans = 1
while k <= n:
    if str(k) == str(k)[::-1]:
        ans = k
    x += 1
    k = x**3

print(ans)