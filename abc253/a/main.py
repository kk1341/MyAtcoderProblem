#!/usr/bin/env python3
A = list(map(int, input().split()))
B = sorted(A)

print('Yes') if A[1] == B[1] else print('No')