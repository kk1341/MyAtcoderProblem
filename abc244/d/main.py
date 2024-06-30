#!/usr/bin/env python3
s = list(map(str, input().split()))
t = list(map(str, input().split()))
change = 0

for i in range(len(s)):
    if s[i] != t[i]:
        change += 1

if change == 0 or change == 3:
    print('Yes')
else:
    print('No')