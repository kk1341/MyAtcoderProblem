#!/usr/bin/env python3
a, b, c, d = map(int, input().split())
ans = 'Takahashi'

if a > c:
    ans = 'Aoki'
elif a == c:
    if b > d:
        ans = 'Aoki'

print(ans)
