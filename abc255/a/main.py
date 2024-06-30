#!/usr/bin/env python3
r,c = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(2)]
print(A[r-1][c-1])