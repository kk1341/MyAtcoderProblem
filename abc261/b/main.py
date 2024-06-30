#!/usr/bin/env python3
n = int(input())
A = []
for i in range(n):
    s = input()
    A.append(list(s))
ans = 'correct'

for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        if  A[i][j] == 'W' and A[j][i] == 'L':
            continue
        elif A[i][j] == 'L' and A[j][i] == 'W':
            continue
        elif A[i][j] == 'D' and A[j][i] == 'D':
            continue
        else:
            ans = 'incorrect'

print(ans)