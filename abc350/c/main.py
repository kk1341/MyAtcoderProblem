#!/usr/bin/env python3
n = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

pos = [0]*n
for i in range(n):
    pos[A[i]] = i

ans = []
for i in range(n):
    j = pos[i]
    if j == i:
        continue
    else:
        A[j], A[i] = A[i], A[j]
        pos[A[i]], pos[A[j]] = pos[A[j]], pos[A[i]]
        ans.append([min(i, j)+1, max(i, j)+1])

print(len(ans))
for res in ans:
    print(*res)