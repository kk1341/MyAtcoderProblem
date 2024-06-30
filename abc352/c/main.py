#!/usr/bin/env python3
N = int(input())
A = []

m = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    m = max(m, b-a)

print(m + sum(A))