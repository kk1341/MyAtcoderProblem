#!/usr/bin/env python3
s = input()
top = 0
end = 0

for c in s:
    if c != 'a':
        break
    top += 1

for c in s[::-1]:
    if c != 'a':
        break
    end += 1

S = (end - top) * 'a' + s
if top <= end and S == S[::-1]:
    print('Yes')
else:
    print('No')