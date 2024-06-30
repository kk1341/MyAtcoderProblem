#!/usr/bin/env python3
import bisect
n = int(input())
A = list(map(int, input().split()))
person = []

for i in range(n):
    person.append([A[i], i+1])

A.sort()
person = sorted(person, key=lambda x: x[0])
ans = [person[0][1]]

for i in range(1, n):
    key = bisect.bisect_left(A, ans[-1])
    ans.append(person[key][1])

print(*ans)