#!/usr/bin/env python3
n = int(input())
print('Yes' if -2**31 <= n and n < 2**31 else 'No')