#!/usr/bin/env python3
h, w = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(h)]

for i in range(w):
    for j in range(h):
        print(A[j][i], end=' ')
    print()