#!/usr/bin/env python3
m = int(input())
D = list(map(int, input().split()))
mid = (sum(D)+1) // 2

for i in range(m):
    if mid <= D[i]:
        print(i+1, mid)
        exit()
    else:
        mid -= D[i]