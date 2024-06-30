#!/usr/bin/env python3
import math
n = int(input())
ans = 0

a = 1
while True:
    if n < math.factorial(a):
        break
    a += 1

for i in range(a-1, 0, -1):
    cnt = 0
    cnt += n // math.factorial(i)
    ans += cnt
    n -= math.factorial(i) * cnt

print(ans)