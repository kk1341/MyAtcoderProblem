#!/usr/bin/env python3
n, t = map(int, input().split())
s = input()
T = list(map(int, input().split()))
x1, x2 = [], []

for i in range(len(s)):
    if s[i] == '1':
        x1.append(T[i])
    else:
        x2.append(T[i])

x1.sort()
x2.sort()

ans, l, r = 0, 0, 0
for i in range(len(x1)):
    while l < len(x2) and x2[l] < x1[i]:
        l += 1
    while r < len(x2) and x2[r] <= x1[i] + 2 * t:
        r += 1
    ans += (r - l)

print(ans)