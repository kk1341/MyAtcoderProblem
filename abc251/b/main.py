#!/usr/bin/env python
n, w = map(int, input().split())
A = list(map(int, input().split()))
ans = []

def jugue(A):
    if sum(A) <= w:
        return ans.append(sum(A))

for i in range(n):
    jugue([A[i]])
    for j in range(i+1, n):
        jugue([A[i], A[j]])
        for k in range(j+1, n):
            jugue([A[i], A[j], A[k]])

print(len(set(ans)))