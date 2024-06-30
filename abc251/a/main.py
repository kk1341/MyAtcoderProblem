#!/usr/bin/env python3
s = input()
ans = ''
for i in range(6 // len(s)):
    ans += s

print(ans)