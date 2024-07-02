#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
days = list(range(1, n+1))

index = 0
for i in range(n):
    print(A[index]-days[i])
    if days[i] == A[index]:
        index += 1