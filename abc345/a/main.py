#!/usr/bin/env python3
s = input()
s1 = s[0]
s2 = s[-1]
if s1 == '<' and s2 == '>' and s[1:len(s)-1].count('=') == len(s)-2:
    print('Yes')
else:
    print('No')