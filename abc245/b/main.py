#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
A.sort()
a = list(set(A))

for i in range(len(a)):
    if i != a[i]:
        print(i)
        exit()

print(a[-1]+1)