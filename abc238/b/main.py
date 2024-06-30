#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
cur = 0
cut = [0, 360]

for i in range(n):
    cur = (cur + A[i]) % 360
    cut.append(cur)

cut.sort()
ans = 0
for i in range(len(cut)-1):
    if ans < cut[i+1] - cut[i]:
        ans = cut[i+1] - cut[i]

print(ans)