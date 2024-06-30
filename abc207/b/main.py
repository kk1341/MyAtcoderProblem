#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
skyblue = a
red = 0
ans = -1

for i in range(a+1):
    if skyblue <= d * red:
        ans = i
        break
    skyblue += b
    red += c

print(ans)