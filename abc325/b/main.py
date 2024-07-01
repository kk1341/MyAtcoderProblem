#!/usr/bin/env python3

n = int(input())
wx = [[int(x) for x in input().split()] for _ in range(n)]

ans = 0
for i in range(24):
    human = 0
    for j in range(n):
        t = (i + wx[j][1]) % 24
        if 9 <= t <= 17:
            human += wx[j][0]
    
    ans = max(ans, human)

print(ans)