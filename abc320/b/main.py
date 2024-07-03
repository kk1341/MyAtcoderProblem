#!/usr/bin/env python3
s = input()
ans = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        new_s = s[i:j]
        if new_s == new_s[::-1]:
            ans = max(ans, len(new_s))

print(ans)