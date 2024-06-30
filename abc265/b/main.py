#!/usr/bin/env python3
n, m, t = map(int, input().split())
A = list(map(int, input().split()))
X = [[int(x) for x in input().split()] for _ in range(m)]

bouns_index = 0
for i in range(n-1):
    if t - A[i] > 0:
        t -= A[i]
        if bouns_index < m and X[bouns_index][0]-1 == i+1:
            t += X[bouns_index][1]
            bouns_index += 1
    else:
        print('No')
        exit()

print('Yes')