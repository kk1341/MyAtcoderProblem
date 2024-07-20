#!/usr/bin/env python3
n = int(input())
S = set()

for i in range(n):
    s = input()
    if s in S or s[::-1] in S:
        continue
    else:
        S.add(s)

print(len(S))