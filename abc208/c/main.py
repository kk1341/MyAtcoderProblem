#!/usr/bin/env python3
n, k = map(int, input().split())
A = list(map(int, input().split()))
sort_A = sorted(A)
dict_A = {}

for i in range(len(A)):
    dict_A[A[i]] = 0

a = k // n
b = k % n

for i in range(b):
    dict_A[sort_A[i]] += 1

for i in dict_A.values():
    print(a + i)
