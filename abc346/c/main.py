#!/usr/bin/env python3
n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if A[i] > k:
        A[i] = 0

A = list(set(A))
K = k*(k+1) // 2
print(K - sum(A))