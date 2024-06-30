#!/usr/bin/env python3
n, k, x = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
max_index = 0
index = 1

for i in range(k):
    if A[max_index] == 0:
        break
    if A[max_index] < A[index]:
        A[index] = max(A[index]-x, 0)
        if index < len(A)-1:
            index += 1
    else:
        A[max_index] = max(A[max_index]-x, 0)
        if A[max_index] == 0:
            max_index += 1

print(sum(A))