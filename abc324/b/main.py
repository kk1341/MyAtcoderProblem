#!/usr/bin/env python3

n = int(input())

for x in range(50):
    for y in range(50):
        if n == 2**x * 3**y:
            print('Yes')
            exit()

print('No')