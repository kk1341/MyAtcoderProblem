#!/usr/bin/env python3
n, m = map(int, input().split())
S = [[s for s in input()] for _ in range(n)]

ans = n
for i in range(2**n):
    exist = [False] * m
    cnt = 0
    for j in range(n):
        if (i >> j) & 1:
            cnt += 1
            for k in range(m):
                if S[j][k] == 'o':
                    exist[k] = True
    
    all_exist = True
    for j in range(m):
        if not exist[j]:
            all_exist = False
    if all_exist:
        ans = min(ans, cnt)

print(ans)