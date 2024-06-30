#!/usr/bin/env python3

x, y = map(int, input().split())
ans = 0

while True:
    if x >= y:
        break
    x += 10
    ans += 1

print(ans)