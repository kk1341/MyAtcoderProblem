#!/usr/bin/env python3
n, q = map(int, input().split())
s = input()
A = []
B = [0]

for i in range(n-1):
    if s[i] == s[i+1]:
        A.append(1)
    else:
        A.append(0)


for i in range(len(A)):
    B.append(A[i] + B[i])

for i in range(q):
    l, r = map(int, input().split())
    print(B[r-1] - B[l-1])
