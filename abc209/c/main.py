#!/usr/bin/env python3
n = int(input())
C = list(map(int, input().split()))
C.sort()
ans = 1

for i in range(n):
    ans  = ans * max(0, C[i] - i) % 1000000007

print(ans)