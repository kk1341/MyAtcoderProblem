#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
S = []
S_dict = defaultdict(int)

for i in range(n):
    s = input()
    if s not in S_dict:
        print(s)
        S_dict[s] += 1
    else:
        print(f'{s}({S_dict[s]})')
        S_dict[s] += 1
