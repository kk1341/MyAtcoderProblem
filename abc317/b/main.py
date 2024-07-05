#!/usr/bin/env python3
n = int(input())
A = sorted(list(map(int, input().split())))
start = min(A)
end = max(A)

for i in range(start, end+1):
    if A[i-start] != i:
        print(i)
        exit()