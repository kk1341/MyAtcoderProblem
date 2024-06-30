#!/usr/bin/env python3

l, r = map(int ,input().split())
s = input()
ans = s[:l-1]
tmp = s[l-1:r]
ans += (tmp[::-1] + s[r:])
print(ans)
