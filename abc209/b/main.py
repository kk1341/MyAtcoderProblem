#!/usr/bin/env python3
n, x = map(int, input().split())
A = list(map(int, input().split()))

money = 0
for i in range(n):
    if i % 2 == 0:
        money += A[i]
    else:
        money += A[i] - 1

print('Yes' if x >= money else 'No')