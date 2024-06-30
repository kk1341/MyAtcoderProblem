#!/usr/bin/env python3
x1, y1, x2, y2 = map(int, input().split())
length_5 = [[1, 2],
            [2, 1],
            [-1, 2],
            [-2, 1],
            [1, -2],
            [2, -1],
            [-1, -2],
            [-2, -1],]
a = []
b = []

for i in range(len(length_5)):
    a.append([x1 + length_5[i][0], y1 + length_5[i][1]])
    b.append([x2 + length_5[i][0], y2 + length_5[i][1]])

ans = 'No'
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            ans = 'Yes'

print(ans)