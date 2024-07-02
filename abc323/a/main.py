#!/usr/bin/env python3

s = input()
for i in range(0, 16, 2):
    if s[i+1] == '1':
        print('No')
        exit()

print('Yes')