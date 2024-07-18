#!/usr/bin/env python3
from collections import defaultdict
s = input()
d = defaultdict(int)

c = 'a'
for i in range(26):
    d[c] = 0
    c = chr(ord(c)+1)

for i in range(len(s)):
    d[s[i]] += 1

ans = len(s) * len(s)
same = False
c = 'a'
for i in range(26):
    if c not in d:
        c = chr(ord(c)+1)
        continue
    ans -= d[c] * d[c]
    if d[c] > 1:
        same = True
    c = chr(ord(c)+1)

ans //= 2
if same:
    ans += 1

print(ans)