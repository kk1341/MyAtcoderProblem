#!/usr/bin/env python3

A = [[int(x) for x in input().split()] for i in range(3)]
x = []
y = []
ans_x = 0
ans_y = 0
for i in range(3):
    x.append(A[i][0])
    y.append(A[i][1])

for i in range(3):
    if x.count(x[i]) == 1:
        ans_x = x[i]
    if y.count(y[i]) == 1:
        ans_y = y[i]

print(f'{ans_x} {ans_y}')