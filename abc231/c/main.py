#!/usr/bin/env python3
from collections import defaultdict
import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for i in range(q)]

A.sort()
sort_x = sorted(X)
dict_x = defaultdict(int)

index = 0
for i in range(q):
    index = bisect.bisect_left(A, sort_x[i])
    dict_x[sort_x[i]] = len(A) - index

for i in range(q):
    print(dict_x[X[i]])