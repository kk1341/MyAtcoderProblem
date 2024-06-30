#!/usr/bin/env python3
import math
n = int(input())
A = [[int(x) for x in input().split()] for i in range(n)]
ans = 0

for i in range(n):
    x1 = A[i][0]
    y1 = A[i][1]
    for j in range(i+1, n):
        x2 = A[j][0]
        y2 = A[j][1]
        length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if ans <= length:
            ans = length
    
print(ans)