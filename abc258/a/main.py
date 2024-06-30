#!/usr/bin/env python3
k = int(input())

h = str(21 + k // 60)
m = ''
if k % 60 < 10:
    m = '0' + str(k%60)
else:
    m = str(k%60)
print(f'{h}:{m}')