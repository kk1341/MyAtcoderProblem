#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

print('Yes' if A.count(A[0]) == n else 'No')