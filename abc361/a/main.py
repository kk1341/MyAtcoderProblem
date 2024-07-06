#!/usr/bin/env python3

n, k, x = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(n):
    if i == k:
        ans.append(x)
    ans.append(A[i])

if n == k:
    ans.append(x)
print(*ans)