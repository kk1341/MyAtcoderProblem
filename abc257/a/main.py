#!/usr/bin/env python3
n, x = map(int, input().split())
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_alp = ''
for i in range(len(alp)):
    new_alp += alp[i] * n

print(new_alp[x-1])