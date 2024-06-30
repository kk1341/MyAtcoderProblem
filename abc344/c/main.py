#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
l = int(input())
C = list(map(int, input().split()))
q = int(input())
X = list(map(int, input().split()))

all_sum = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            all_sum.add(A[i] + B[j] + C[k])

for x in X:
    if x in all_sum:
        print('Yes')
    else:
        print('No')