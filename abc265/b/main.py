#!/usr/bin/env python3
n, m, t = map(int, input().split())
A = list(map(int, input().split()))
X = [[int(x) for x in input().split()] for _ in range(m)]

cnt = 1
index = 0
ans = 'Yes'
while index < n:
    t -= A[index]
    if X[index][0] == cnt:
        t += X[index][1]
    if t <= 0:
        ans = 'No'
        break
    cnt += 1
    index += 1

print(ans)