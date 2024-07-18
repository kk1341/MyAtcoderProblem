#!/usr/bin/env python3
n = int(input())
A = sorted(list(map(int, input().split())))

r = n
cnt, ans = 0, 0
for i in range(n):
    r = max(r, i+1)
    while r - 1 > i and A[i] + A[r-1] >= 10**8:
        r -= 1
    cnt += (n - r)

for i in range(n):
    ans += (n-1) * A[i]

ans -= 10**8 * cnt
print(ans)