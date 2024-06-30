#!/usr/bin/env python3
import sys
s = input()
t = input()
ans = 'Yes'

k = (ord(t[0]) - ord(s[0])) % 26

for i in range(len(s)):
    k1 = (ord(t[i]) - ord(s[i])) % 26
    if k != k1:
        ans = 'No'
        break
    
print(ans)
