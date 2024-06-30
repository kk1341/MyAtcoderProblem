#!/usr/bin/env python3
s = input()
flag = [0, 0, 1]
for i in range(len(s)):
    if ord('A') <= ord(s[i]) <= ord('Z'):
        flag[0] = 1
    if ord('a') <= ord(s[i]) <= ord('z'):
        flag[1] = 1
    if s.count(s[i]) != 1:
        flag[2] = 0

if flag == [1, 1, 1]:
    print('Yes')
else:
    print('No')