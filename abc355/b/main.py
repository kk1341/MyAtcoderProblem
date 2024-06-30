#!/usr/bin/env python3
n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(A+B)


ans = 'No'
for i in range(len(A)-1):
    for j in range(len(C)-1):
        if A[i] == C[j] and A[i+1] == C[j+1]:
            ans = 'Yes'

print(ans)