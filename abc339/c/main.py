#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))

now_person = [0] * n
now_person[0] = A[0]
for i in range(n-1):
    now_person[i+1] = now_person[i] + A[i+1] 

start = abs(min(0, min(now_person)))
print(start + sum(A))
