#!/usr/bin/env python3
n = int(input())
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        s1, s2 = A[i], B[i]
        if s1[j] != s2[j]:
            print(i+1, j+1)
            exit()