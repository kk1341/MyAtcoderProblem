#!/usr/bin/env python3
a,b,k = map(int, input().split())
ans = 0
while True:
    if a >= b:
        break
    a *= k
    ans += 1

print(ans)