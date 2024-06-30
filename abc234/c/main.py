#!/usr/bin/env python3
k = int(input())
bin_str = format(k, 'b')
ans = ''
for i in range(len(bin_str)):
    if bin_str[i] == '1':
        ans += '2'
    else:
        ans += '0'

print(ans)