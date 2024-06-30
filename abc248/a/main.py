#!/usr/bin/env python3

s = list(input())
s.sort()
ans = 9
for i in range(len(s)):
    if s[i] != str(i):
        ans = i
        break

print(ans)