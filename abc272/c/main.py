#!/usr/bin/env python3

n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
odd = []
even = []

for i in range(n):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])

ans = -1
if len(odd) >= 2:
    ans = max(ans, odd[0] + odd[1])
if len(even) >= 2:
    ans = max(ans, even[0] + even[1])

print(ans)