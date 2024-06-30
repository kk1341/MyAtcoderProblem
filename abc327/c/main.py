#!/usr/bin/env python3
A = [[int(x) for x in input().split()] for _ in range(9)]
ans_list = sorted(list(range(1, 10)))
flag = True

for i in range(9):
    S = set(A[i])
    if len(S) != 9:
        flag = False

for i in range(9):
    S = set([row[i] for row in A])
    if len(S) != 9:
        flag = False

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        S = set()
        for i2 in range(i, i+3):
            for j2 in range(j, j+3):
                S.add(A[i2][j2])
        
        if len(S) != 9:
            flag = False

print('Yes' if flag else 'No')
