#!/usr/bin/env python3
n = int(input())
s = input()
ans = 'Takahashi'

for i in range(n):
    if s[i] == '1':
        break
    elif ans == 'Takahashi':
        ans = 'Aoki'
    else:
        ans = 'Takahashi'

print(ans)