#!/usr/bin/env python3
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_a = max(A)
ans = 'No'
for i in range(n):
    if A[i] == max_a and (i+1 in B):
        ans = 'Yes'
        break

print(ans)