#!/usr/bin/env python3

n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))

index = 0
a = n - k - 1
ans = 10**9
while index + a < n:
    ans = min(A[index+a] - A[index], ans)
    index += 1

print(ans)