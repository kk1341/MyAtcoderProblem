#!/usr/bin/env python3
n = int(input())
factors = []
for i in range(1, 10):
    if n % i == 0:
        factors.append(i)

ans = ''
for i in range(n+1):
    flag = False
    for factor in factors:
        if i % (n//factor) == 0:
            flag = True
            ans += str(factor)
            break
    if not flag:
        ans += '-'

print(ans)