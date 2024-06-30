#!/usr/bin/env python3
n = int(input())
p = list(map(int, input().split()))

ans = 0
index = n-2
while True:
    if p[index] == 1:
        ans += 1
        break
    else:
        index = p[index]-2
        ans += 1

print(ans)