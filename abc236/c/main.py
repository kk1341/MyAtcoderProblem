#!/usr/bin/env python3
n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
station = {}

for i in range(n):
    station[s[i]] = 0

for i in range(m):
    if t[i] in station:
        station[t[i]] = 1

for i in range(n):
    if station[s[i]] == 1:
        print('Yes')
    else:
        print('No')