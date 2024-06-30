#!/usr/bin/env python3
n = int(input())
if n % 100 == 0:
    print(n // 100)
else:
    print(n // 100 + 1)