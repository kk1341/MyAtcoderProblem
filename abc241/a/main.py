#!/usr/bin/env python3
A = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans = A[ans]

print(ans)